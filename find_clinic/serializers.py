from rest_framework import serializers
from find_clinic.models import ClinicCategoriyes, Clinics, Consultation
from authentification.models import CustomUser
from django.db.models import Q


class ClinicCategoriyesSerializers(serializers.ModelSerializer):
    class Meta:
        model = ClinicCategoriyes
        fields = ['id', 'name_categories', 'icon_categories']


class ClinicCategoriyesCrudSerializers(serializers.ModelSerializer):
    icon_categories = serializers.ImageField(
        max_length=None,
        allow_empty_file=False,
        allow_null=False,
        use_url=False,
        required=False,
    )
    class Meta:
        model = ClinicCategoriyes
        fields = ['id', 'name_categories', 'icon_categories']
    

    def create(self, validated_data):
        create = ClinicCategoriyes.objects.create(**validated_data)
        create.save()
        return create

    def update(self, instance, validated_data):
        instance.name_categories = validated_data.get("name_categories", instance.name_categories)
        if instance.icon_categories == None:
            instance.icon_categories = self.context.get("icon_categories")
        else:
            instance.icon_categories = validated_data.get("icon_categories", instance.icon_categories)
        instance.save()
        return instance


class ClinicsSerializers(serializers.ModelSerializer):
    id_categories = ClinicCategoriyesSerializers(read_only=True)
    class Meta:
        model = Clinics
        fields = '__all__'


class ClinicCrudSerializers(serializers.ModelSerializer):
    logo_clinic = serializers.ImageField(
        max_length=None,
        allow_empty_file=False,
        allow_null=False,
        use_url=False,
        required=False,
    )
    class Meta:
        model = Clinics
        fields = ['id', 'name_clinic', "about_clinic", "price", "patients", "experiences", "user_id", "id_categories", "rating", "location", 'icon_categories']
    

    def create(self, validated_data):
        create = Clinics.objects.create(**validated_data)
        create.user_id = self.context.get("user_id")
        create.save()
        return create

    def update(self, instance, validated_data):
        instance.name_clinic = validated_data.get("name_clinic", instance.name_clinic)
        instance.about_clinic = validated_data.get("about_clinic", instance.about_clinic)
        instance.price = validated_data.get("price", instance.price)
        instance.patients = validated_data.get("patients", instance.patients)
        instance.experiences = validated_data.get("experiences", instance.experiences)
        instance.user_id = validated_data.get("user_id", instance.user_id)
        instance.id_categories = validated_data.get("id_categories", instance.id_categories)
        instance.rating = validated_data.get("rating", instance.rating)
        instance.location = validated_data.get("location", instance.location)
        if instance.logo_clinic == None:
            instance.logo_clinic = self.context.get("logo_clinic")
        else:
            instance.logo_clinic = validated_data.get("logo_clinic", instance.logo_clinic)
        instance.save()
        return instance


class UserListSerializers(serializers.ModelSerializer):
    """User Serializers"""

    class Meta:
        """User Fields"""

        model = CustomUser
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
        )


class ConsultationSerializers(serializers.ModelSerializer):
    """Consultation Serializers"""
    clinic_id = ClinicsSerializers(read_only=True)
    doctor_id = UserListSerializers(read_only=True)
    user_id = UserListSerializers(read_only=True)

    class Meta:
        """Consultation Fields"""

        model = Consultation
        fields = "__all__"


class ConsultationPostSerializers(serializers.ModelSerializer):
    """Consultation POST Serializers"""

    class Meta:
        """Consultation Fields"""

        model = Consultation
        fields = "__all__"

    def create(self, validated_data):
        """Consultation POST"""
        check_date = (
            Consultation.objects.select_related("clinic_id")
            .filter(clinic_id=validated_data["clinic_id"])
            .filter(
                Q(appoint_date__day=validated_data["appoint_date"].strftime("%Y"))
                | Q(appoint_date__day=validated_data["appoint_date"].strftime("%m"))
                | Q(appoint_date__day=validated_data["appoint_date"].strftime("%d"))
            )
            .filter(Q(appoint_time__hour=validated_data["appoint_time"].strftime("%H")))
        )

        if bool(check_date):
            raise serializers.ValidationError("The doctor is busy at the moment")
        else:
            create = Consultation.objects.create(**validated_data)
            create.user_id = self.context.get("user_id")
            create.save()
        return create

    def update(self, instance, validated_data):
        """Update Consultation"""
        instance.appoint_time = validated_data.get("appoint_time", instance.appoint_time)
        check_date = (
            Consultation.objects.select_related("clinic_id")
            .filter(clinic_id=validated_data["clinic_id"])
            .filter(
                Q(appoint_date__day=validated_data["appoint_date"].strftime("%Y"))
                | Q(appoint_date__day=validated_data["appoint_date"].strftime("%m"))
                | Q(appoint_date__day=validated_data["appoint_date"].strftime("%d"))
            )
            .filter(Q(appoint_time__hour=validated_data["appoint_time"].strftime("%H")))
        )

        if bool(check_date):
            raise serializers.ValidationError("The doctor is busy at the moment")
        else:
            instance.appoint_date = validated_data.get("appoint_date", instance.appoint_date)
            instance.doctor_id = validated_data.get("doctor_id", instance.doctor_id)
            instance.save()
        return instance