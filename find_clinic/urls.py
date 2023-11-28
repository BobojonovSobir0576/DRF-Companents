from django.urls import path
from find_clinic.views import (
    ClinicCategoriyesViews,
    ClinicCategoriyesCRUDViews,
    ClinicsViews,
    ClinicCRUDViews,
    ClinicInCategoriesViews,
    ConsultationClinicViews,
    ConsultationCrudViews,
    ConsultationUserHistoryViews,
)

urlpatterns = [
    path('clinic_categoriyes_views/', ClinicCategoriyesViews.as_view()),
    path('clinic_categoriyes_crud_views/<int:pk>/', ClinicCategoriyesCRUDViews.as_view()),
    path('clinics_views/', ClinicsViews.as_view()),
    path('clinic_crud_views/<int:pk>/', ClinicCRUDViews.as_view()),
    path('clinic_incategories_views/<int:pk>/', ClinicInCategoriesViews.as_view()),
    path('consultation_clinic_views/', ConsultationClinicViews.as_view()),
    path('consultation_crud_views/<int:pk>/', ConsultationCrudViews.as_view()),
    path('consultation_user_history_views/', ConsultationUserHistoryViews.as_view()),
]