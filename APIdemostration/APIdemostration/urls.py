"""
URL configuration for APIdemostration project.

Including URL patterns from the library application.
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns  
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("library/", include("library.urls")),  # Include URL patterns from library app
]
