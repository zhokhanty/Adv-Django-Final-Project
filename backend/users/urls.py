from django.urls import path
from .views import verify_2fa, setup_2fa

urlpatterns = [
    path('2fa/setup/', setup_2fa, name='setup-2fa'),
    path('2fa/verify/', verify_2fa, name='verify-2fa'),
]