from django.db import models
from authentification.models import CustomUser

class ClinicCategoriyes(models.Model):
    name_categories = models.CharField(max_length=80, null=True, blank=True)
    icon_categories = models.ImageField(upload_to='icon_categories/', null=True, blank=True)

    def __str__(self):
        return self.name_categories

class Clinics(models.Model):
    name_clinic = models.CharField(max_length=250, null=True, blank=True)
    logo_clinic = models.ImageField(upload_to='logo_clinic/', null=True, blank=True)
    about_clinic = models.TextField(null=True, blank=True)
    price = models.CharField(max_length=10, null=True, blank=True)
    patients = models.IntegerField(null=True, blank=True)
    experiences = models.IntegerField(null=True, blank=True)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    id_categories = models.ForeignKey(ClinicCategoriyes, on_delete=models.CASCADE, null=True, blank=True)
    rating = models.CharField(max_length=50, null=True, blank=True)
    location = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name_clinic


class Consultation(models.Model):
    clinic_id = models.ForeignKey(
        Clinics,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="clinic_id")
    user_id = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="user_id")
    appoint_date = models.DateField(null=True, blank=True,)
    appoint_time = models.TimeField(null=True, blank=True,)
    create_date = models.DateTimeField(auto_now_add=True)