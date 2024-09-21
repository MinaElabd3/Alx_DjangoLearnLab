from django.urls import path
from .views import RegisterView, LoginView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]

from django.urls import path
from .views import follow_user, unfollow_user

urlpatterns = [
    path('follow/<int:user_id>/', follow_user, name='follow_user'),
    path('unfollow/<int:user_id>/', unfollow_user, name='unfollow_user'),
]

from django.urls import path
from .views import user_feed

urlpatterns = [
    path('feed/', user_feed, name='user_feed'),
]

