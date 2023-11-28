
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.shortcuts import redirect, reverse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status

from fitness.models import (
    Fitness,
    FitnessCreateReservation,
    FitnessCategories,
    FitnessAmenities,
    FitnessReservation,
    FitnessMultipleImageUpload
)

from fitness.serializer.fitness_categories_serializer import (
    FitnessCategoriesSerialzier,
    FitnessAmenitiesSerialzier
)
from fitness.serializer.fitness_serializer import (
    FitnessDeatilsSerializer,
    FitnessListSeralizer
)
from fitness.serializer.fitness_create_reservation_serialzier import (
    FitnessCreateReservationSerializers,
    FitnessDetailsReservationSerializers,
    FitnessReservationSerilaizer
)


class FitnesCategoriesView(APIView):
    def get(self, request):
        quryset = FitnessCategories.objects.all()
        serializer = FitnessCategoriesSerialzier(
            quryset, many=True
        )
        return Response(serializer.data, status=status.HTTP_200_OK)


class FitnesView(APIView):

    def get(self, request):
        queryset = Fitness.objects.all()
        serializer = FitnessDeatilsSerializer(
            queryset, many=True
        )
        return Response(serializer.data, status=status.HTTP_200_OK)


class FitnesFilterView(APIView):

    def get(self, request, id):
        queryset = Fitness.objects.prefetch_related('categories').filter(
            categories__id=id
        )
        if queryset:
            serializer = FitnessDeatilsSerializer(
                queryset, many=True
            )
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)


class FitnesGetViews(APIView):

    def get(self, request, id):
        queryset = get_object_or_404(Fitness, id=id)
        serializer = FitnessDeatilsSerializer(
            queryset
        )
        return Response(serializer.data, status=status.HTTP_200_OK)


class FitnessDetailReservation(APIView):
    def get(self, request, id):
        queryset = FitnessCreateReservation.objects.select_related('fitness').filter(
            fitness=id
        )
        serializer = FitnessCreateReservationSerializers(
            queryset, many=True
        )
        return Response(serializer.data, status=status.HTTP_200_OK)


class FitnessReservationGetView(APIView):

    def get(self, request, id):
        queryset = get_object_or_404(FitnessReservation, fitness=id)
        serializer = FitnessReservationSerilaizer(
            queryset
        )
        return Response(serializer.data, status=status.HTTP_200_OK)

