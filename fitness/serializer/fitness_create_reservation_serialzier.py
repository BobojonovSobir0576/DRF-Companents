from rest_framework import serializers


from authentification.serializers.register_by_email_serializer import (
    UserProfileSerializer
)


from fitness.models import (
    Fitness,
    FitnessCreateReservation,
    FitnessCategories,
    FitnessAmenities,
    FitnessReservation,
    FitnessMultipleImageUpload
)

class FitnessUploadMultipleImagesSerialzier(serializers.ModelSerializer):

    class Meta:
        model = FitnessMultipleImageUpload
        fields = '__all__'


class FitnessDeatilsSerializer(serializers.ModelSerializer):
    images = FitnessUploadMultipleImagesSerialzier(read_only=True, many=True)

    class Meta:
        model = Fitness
        fields = [
            'images',
            'id',
            'title',
            'content',
            'categories',
            'amenities',
            'user',
            'teacher',
            'img',
        ]


class FitnessCreateReservationSerializers(serializers.ModelSerializer):
    user = UserProfileSerializer(many=True, read_only=True)
    class Meta:
        model = FitnessCreateReservation
        fields = [
            'id',
            'fitness',
            'user',
            'timestamp',
            'secondstamp',
        ]

        def create(self, validated_data):
            create = FitnessCreateReservation.obejcts.create(
                **validated_data
            )
            create.fitness = self.context.get('fitness')
            create.save()
            return create


class FitnessDetailsReservationSerializers(serializers.ModelSerializer):
    user = UserProfileSerializer(many=True, read_only=True)
    fitness = FitnessDeatilsSerializer(read_only=True)

    class Meta:
        model = FitnessCreateReservation
        fields = [
            'id',
            'fitness',
            'user',
            'timestamp',
            'secondstamp',
        ]


class FitnessReservationSerilaizer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)
    fitness = FitnessDeatilsSerializer(read_only=True)

    class Meta:
        model = FitnessReservation
        fields = ['id', 'fitness', 'user', 'created_at']

    def create(self, validated_data):
        users = validated_data.pop()

        create = FitnessReservation.objects.create(
             **validated_data
         )

        create.fitness = self.context.get('fitness')
        create.user = self.context.get('user')
        create.save()
        get_fitness = FitnessCreateReservation.objects.get(id=self.context.get('fitness').id)
        for k in users:
            get_fitness.user.add(k)
            get_fitness.save()

        return create

