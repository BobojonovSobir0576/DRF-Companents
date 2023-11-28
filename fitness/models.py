from django.db import models
from authentification.models import (
    CustomUser
)
from twisted.conch.insults.insults import modes


class FitnessCategories(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class FitnessAmenities(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class Fitness(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    content = models.CharField(max_length=255, null=True, blank=True)
    categories = models.ManyToManyField(
        FitnessCategories, null=True,
        blank=True
    )
    amenities = models.ManyToManyField(
        FitnessAmenities, null=True,
        blank=True
    )
    user = models.ManyToManyField(
        CustomUser, null=True,
        blank=True, related_name='user'
    )
    teacher = models.ManyToManyField(
        CustomUser, null=True,
        blank=True, related_name='teacher'
    )
    img = models.ImageField(upload_to='fitness-categories/', null=True, blank=True)

    def __str__(self):
        return self.title


class FitnessMultipleImageUpload(models.Model):
    fitness = models.ForeignKey(
        Fitness, on_delete=models.CASCADE, null=True, blank=True, related_name='images'
    )
    img = models.ImageField(upload_to='fitness-categories/', null=True, blank=True)


class FitnessCreateReservation(models.Model):
    fitness = models.ForeignKey(
        Fitness,
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    user = models.ManyToManyField(
        CustomUser, null=True,
        blank=True, related_name='reservation_user'
    )
    timestamp = models.CharField(max_length=255, null=True, blank=True)
    secondstamp = models.IntegerField(default=30, null=True, blank=True)



    def __str__(self):
        return self.fitness.title


class FitnessReservation(models.Model):
    fitness = models.ForeignKey(
        FitnessCreateReservation,
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    user = models.ForeignKey(
        CustomUser, null=True,
        on_delete=models.CASCADE,
        blank=True
    )
    created_at = models.DateField(
        auto_now_add=True
    )

    def __str__(self):
        return self.fitness.fitness.title