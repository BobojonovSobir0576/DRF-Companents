from rest_framework import generics, permissions, status, views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import update_session_auth_hash

from django.contrib.auth import authenticate, login, logout
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.conf import settings
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_str, smart_str, smart_bytes, DjangoUnicodeDecodeError
from django.contrib.auth.tokens import PasswordResetTokenGenerator

from authentification.serializers.register_by_email_serializer import (
    LogoutSerializer,
    PasswordResetCompleteSerializer,
    PasswordResetSerializer,
    LoginSerializer,
    EmailVerificationSerializer,
    RegisterByEmailSerializer,
    UserProfileSerializer,
    UserDetailSerializers,
    UserInformationSerializers,
    ChangePasswordSerializer,
)
from authentification.utils import (
    Util,
    PasswordReset,
    send_sms
)
from authentification.renderers import (
    UserRenderers
)
from authentification.models import (
    CustomUser,
    SmsCode
)
import jwt, random


def get_token_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
      "refresh": str(refresh),
      "access": str(refresh.access_token)}



class UserSignUpViews(APIView):
    render_classes = [UserRenderers]

    def post(self, request):
        serializer = RegisterByEmailSerializer(data=request.data, context={'avatar': request.FILES.get('avatar', None)})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserSignInViews(APIView):
    """ Views """
    render_classes = [UserRenderers]

    def post(self, request):
        serializer = LoginSerializer(data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            username = request.data["username"]
            password = request.data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                tokens = get_token_for_user(user)
                sms_random = str(random.randint(10000, 99999))
                send_sms(user.username, sms_random)
                code_save = SmsCode(user_id=user, sms_code=sms_random)
                code_save.save()
                return Response(
                    {"token": tokens, "message": "Welcome to the system"},
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {
                        "error": {
                            "none_filed_error": [
                                "This user is not available to the system"
                            ]
                        }
                    },
                    status=status.HTTP_404_NOT_FOUND,
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CheckSmsCode(APIView):
    """ Views """
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]

    def post(self, request):
        sms_code = request.data["sms_code"]
        if sms_code == "":
            context = {"Code not entered"}
            return Response(context, status=status.HTTP_401_UNAUTHORIZED)
        code_objects = SmsCode.objects.latest("id")
        if int(sms_code) == int(code_objects.sms_code):
            context = {"Welcome to the system !"}
            return Response(context, status=status.HTTP_200_OK)
        return Response(
            {"error": "SMS code error"},
            status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION,
        )


class UserProfilesViews(APIView):
    """User Pofiles classs"""

    render_classes = [UserRenderers]
    permission = [IsAuthenticated]

    def get(self, request):
        """User information views"""
        serializer = UserInformationSerializers(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)




@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_password(request):
    if request.method == 'POST':
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            if user.check_password(serializer.data.get('old_password')):
                user.set_password(serializer.data.get('new_password'))
                user.save()
                update_session_auth_hash(request, user)
                return Response(
                    {'message': 'Password changed successfully.'},
                    status=status.HTTP_200_OK
                )
            return Response(
                {'error': 'Incorrect old password.'},
                status=status.HTTP_400_BAD_REQUEST
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)