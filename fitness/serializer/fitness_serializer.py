from rest_framework import serializers


from authentification.serializers.register_by_email_serializer import (
    UserProfileSerializer
)
from fitness.serializer.fitness_categories_serializer import (
    FitnessCategoriesSerialzier,
    FitnessAmenitiesSerialzier
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
    user = UserProfileSerializer(read_only=True, many=True)
    teacher = UserProfileSerializer(read_only=True, many=True)
    categories = FitnessCategoriesSerialzier(read_only=True, many=True)
    amenities = FitnessAmenitiesSerialzier(read_only=True, many=True)

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


class FitnessListSeralizer(serializers.ModelSerializer):
    images = FitnessUploadMultipleImagesSerialzier(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False, use_url=False),
        write_only=True,
    )
    class Meta:
        model = Fitness
        fields = [
            'id',
            'title',
            'content',
            'categories',
            'amenities',
            'user',
            'teacher',
            'img',
            'images'
        ]

    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        create = Fitness.objects.create(**validated_data)
        create.teacher = self.context.get('user')
        create.img = self.context.get('img')
        create.save()

        for i in uploaded_images:
            FitnessMultipleImageUpload.objects.create(
                fitness=create, img=i
            )
        return create