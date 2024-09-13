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

# blog/urls.py
from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]

from django.urls import path
from . import views

urlpatterns = [
    path("post/<int:pk>/comments/new/", views.add_comment, name='add_comment'),
    path("comment/<int:pk>/update/", views.edit_comment, name='edit_comment'),
    path("comment/<int:pk>/delete/", views.delete_comment, name='delete_comment'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('tags/<slug:tag_slug>/', views.posts_by_tag, name='posts_by_tag'),
    path('search/', views.search_posts, name='search_posts'),
        # Search and Tagging URLs
    path('search/', search_posts, name='search-posts'),  # Search posts
    path('tags/<str:tag_name>/', TaggedPostListView.as_view(), name='tagged-posts'),  # Posts by tag
    path('tags/<slug:tag_slug>/', TaggedPostListView.as_view(), name='tagged-posts'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts-by-tag'),  # Posts by tag
]

