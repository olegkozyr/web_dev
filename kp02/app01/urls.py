from django.urls import path
from .views import response, response_text

urlpatterns = [
    path('', response, name='home'),
    path('text/', response_text, name='text'),
]