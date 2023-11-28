from django.urls import path
from fitness.views.views_fitness import (
    FitnesCategoriesView,
    FitnesView,
    FitnesFilterView,
    FitnesGetViews,
    FitnessDetailReservation,
    FitnessReservationGetView
)

urlpatterns = [
    path('fitness-categories/', FitnesCategoriesView.as_view()),
    path('fitness/', FitnesView.as_view()),
    path('fitness-categories-filter/<int:id>/', FitnesFilterView.as_view()),
    path('fitness-first-get/<int:id>/', FitnesGetViews.as_view()),
    path('fitness-detail-reservation/<int:id>/', FitnessDetailReservation.as_view()),
    path('fitness-first-get-reservation/<int:id>/', FitnessReservationGetView.as_view()),
]