from django.urls import path

from .views import (
    RegistrationAPIView,
    LoginAPIView,
    LogoutApiView,
)

urlpatterns = [
    path('registration/', RegistrationAPIView.as_view(), name="registration_email"),
    path('login/', LoginAPIView.as_view(), name="login"),
    path('logout/', LogoutApiView.as_view(), name='logout'),
]
