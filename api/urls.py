from .views import Retrieve_api
from django.urls import path

urlpatterns = [
    path('info/', Retrieve_api),
]
