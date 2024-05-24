from django.urls import path, include
from .views import authView, home

urlpatterns = [
 path("signup/", authView, name="authView"),
 path("", include("django.contrib.auth.urls")),
 
]
