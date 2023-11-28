""" Django DRF Packaging """
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from authentification.renderers import UserRenderers
from find_clinic.models import (
    ClinicCategoriyes,
    Clinics,
    Consultation
)
from find_clinic.serializers import (
    ClinicCategoriyesSerializers,
    ClinicCategoriyesCrudSerializers,
    ClinicsSerializers,
    ClinicCrudSerializers,
    ConsultationSerializers,
    ConsultationPostSerializers,
)

class ClinicCategoriyesViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]
    def get(self, request):
        objects_list = ClinicCategoriyes.objects.all()
        serializers = ClinicCategoriyesSerializers(objects_list, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ClinicCategoriyesCrudSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClinicCategoriyesCRUDViews(APIView):
    render_classes = [UserRenderers]
    permission = [IsAuthenticated]

    def get(self, request, pk):
        objects_list = ClinicCategoriyes.objects.filter(id=pk)
        serializer = ClinicCategoriyesSerializers(objects_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        queryset = get_object_or_404(Clinics, id=pk)
        serializer = ClinicCategoriyesCrudSerializers(
            instance=queryset,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            {"error": "update error data"}, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        objects_get = ClinicCategoriyes.objects.get(id=pk)
        objects_get.delete()
        return Response(
            {"message": "Delete success"}, status=status.HTTP_200_OK
        )
        

class ClinicsViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]
    def get(self, request):
        objects_list = Clinics.objects.all()
        serializers = ClinicsSerializers(objects_list, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ClinicCrudSerializers(
            data=request.data,
            context={
                "user_id": request.user,
            },
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClinicCRUDViews(APIView):
    render_classes = [UserRenderers]
    permission = [IsAuthenticated]

    def get(self, request, pk):
        objects_list = Clinics.objects.filter(id=pk)
        serializer = ClinicsSerializers(objects_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        queryset = get_object_or_404(Clinics, id=pk)
        serializer = ClinicCategoriyesCrudSerializers(
            instance=queryset,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            {"error": "update error data"}, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        objects_get = Clinics.objects.get(id=pk)
        objects_get.delete()
        return Response(
            {"message": "Delete success"}, status=status.HTTP_200_OK
        )


class ClinicInCategoriesViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]
    def get(self, request, pk):
        objects_list = Clinics.objects.filter(id_categories=pk)
        serializers = ClinicsSerializers(objects_list, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


class ConsultationClinicViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]
    def get(self, request):
        objects_list = Consultation.objects.filter(clinic_id__user_id=request.user.id)
        serializers = ConsultationSerializers(objects_list, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        """Consultation POST views"""
        serializer = ConsultationPostSerializers(
            data=request.data,
            context={
                "user_id": request.user,
            },
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConsultationCrudViews(APIView):
    """Consultation CRUD Class"""

    render_classes = [UserRenderers]
    permission = [IsAuthenticated]

    def get(self, request, pk):
        """Consultation GET views"""
        objects_list = Consultation.objects.filter(
            id=pk
        )
        serializer = ConsultationSerializers(objects_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        """Consultation Update views"""
        queryset = get_object_or_404(Consultation, id=pk)
        serializer = ConsultationPostSerializers(
            instance=queryset,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            {"error": "update error data"}, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        """Expeected Salary Delete views"""
        objects_get = Consultation.objects.get(id=pk)
        objects_get.delete()
        return Response(
            {"message": "Delete success"},
            status=status.HTTP_200_OK
        )


class ConsultationUserHistoryViews(APIView):
    """Consultation List Class"""

    render_classes = [UserRenderers]
    permission = [IsAuthenticated]

    def get(self, request):
        """Consultation GET views"""
        objects_list = Consultation.objects.filter(user_id=request.user.id)
        serializer = ConsultationSerializers(objects_list, many=True)
        return Response(
            {"history": serializer.data},
            status=status.HTTP_200_OK
        )