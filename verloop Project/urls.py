from django.urls import path
from .views import getAddressDetails

# adding router to hit api endpoint
urlpatterns = [
    path('getAddressDetails/', getAddressDetails)
]