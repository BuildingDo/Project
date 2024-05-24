from django.contrib import admin
from .models import Symptom, Disease

admin.site.register(Symptom)
admin.site.register(Disease)