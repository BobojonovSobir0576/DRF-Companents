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


class FitnessCategoriesSerialzier(serializers.ModelSerializer):

    class Meta:
        model = FitnessCategories
        fields = "__all__"


class FitnessAmenitiesSerialzier(serializers.ModelSerializer):
    class Meta:
        model = FitnessAmenities
        fields = "__all__"

