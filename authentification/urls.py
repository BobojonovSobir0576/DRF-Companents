from django.urls import path
from authentification.views.register_by_email_views import (
    RegisteByEmailView,
    VerifyEmail,
    LoginApiView,
    UserProfileView,
    UserDetailView,
    RequestPasswordRestEmail,
    PasswordTokenCheckView,
    SetNewPasswordView,
    LogoutView
)

from authentification.views.register_by_sms_views import (
    UserSignUpViews,
    UserSignInViews,
    CheckSmsCode,
    UserProfilesViews,
    change_password,
)

from authentification.socail.views import (
    FacebookSocialAuthView,
    GoogleSocialAuthView,
    FacebookLogin,
    FacebookSignup,
    GitHubLogin,
    GoogleLogin,
    FacebookLoginTwo,
    GoogleView,
    GoogleJw
)
from authentification.fac import FacebookTokenView



urlpatterns = [
    # authentification by email
    path('register-by-email/', RegisteByEmailView.as_view(),name='register'),
    path('login-by-email/', LoginApiView.as_view(), name='login'),
    path('profile-by-email/', UserProfileView.as_view(), name='profile'),
    path('email-verify-by-email/', VerifyEmail.as_view(),name='email-verify'),
    path('detail-by-email/', UserDetailView.as_view(),name='detail'),
    path('request-rest-email-by-email/', RequestPasswordRestEmail.as_view(), name='request-reset-email'),
    path('password-reset-by-email/<uidb64>/<token>/', PasswordTokenCheckView.as_view(), name='password-reset-confirm'),
    path('reset_password_complete-by-email/', SetNewPasswordView.as_view(), name='password_reset_complete'),
    path('logout-by-email/', LogoutView.as_view(), name='logout'),

    # authentification by sms
    path('register-by-sms/', UserSignUpViews.as_view(), name='register-sms'),
    path('login-by-sms/', UserSignInViews.as_view(), name='login-sms'),
    path('check-code-by-sms/', CheckSmsCode.as_view(), name='check-sms'),
    path('facebook/login/', FacebookLogin.as_view()),
    path('facebook/reg/', FacebookSignup.as_view()),
    path('github/login/', GitHubLogin.as_view()),
    path('GoogleView/', GoogleView.as_view()),
    path('GoogleJw/', GoogleJw.as_view()),
    path('user_profiles_views/', UserProfilesViews.as_view()),
    path('change_password/', change_password),

]