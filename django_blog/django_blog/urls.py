"""
URL configuration for django_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# django_blog/urls.py (single project-level)

from django.contrib import admin
from django.urls import path
from blog import views  # Import views from the blog app
from django.contrib.auth import views as auth_views  # Import built-in auth views

urlpatterns = [
    # Admin site
    path('admin/', admin.site.urls),
    
    # Authentication-related URLs
    path('register/', views.register, name='register'),  # Custom view for user registration
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),  # Login view using built-in Django auth
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),  # Logout view
    path('profile/', views.profile, name='profile'),  # Custom view for user profile management
    
    # Other views and URLs can be added here later
]
