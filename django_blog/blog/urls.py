# blog/urls.py

from django.urls import path
from . import views  # Import views from the blog app
from django.contrib.auth import views as auth_views  # Import built-in auth views

urlpatterns = [
    path('register/', views.register, name='register'),  # Registration view
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),  # Login view
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),  # Logout view
    path('profile/', views.profile, name='profile'),  # Profile view
]
