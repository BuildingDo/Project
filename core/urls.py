from django.urls import path
from .views import search_symptoms  # Change the import to match the function name

app_name = 'core'

urlpatterns = [
    path("", search_symptoms, name="search_symptoms"),  # Update the path to use the function name
]

