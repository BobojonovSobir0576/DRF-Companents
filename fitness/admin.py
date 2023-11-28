from django.contrib import admin
from fitness.models import (
    Fitness,
    FitnessCreateReservation,
    FitnessCategories,
    FitnessAmenities,
    FitnessReservation,
    FitnessMultipleImageUpload
)


admin.site.register(Fitness)
admin.site.register(FitnessCreateReservation)
admin.site.register(FitnessCategories)
admin.site.register(FitnessAmenities)
admin.site.register(FitnessReservation)
admin.site.register(FitnessMultipleImageUpload)
