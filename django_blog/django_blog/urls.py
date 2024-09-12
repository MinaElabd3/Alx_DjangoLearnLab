# django_blog/urls.py

from django.contrib import admin
from django.urls import path, include  # Include function is needed to link app URLs

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin URL
    path('', include('blog.urls')),  # Include the app-level URLs from blog/urls.py
]
