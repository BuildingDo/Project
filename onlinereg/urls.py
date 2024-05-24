from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(("base.urls", "base"), "base")), # Added a comma here
    path("search/", include(("core.urls", "core"), "core")),
] + static(settings.STATIC_URL)
