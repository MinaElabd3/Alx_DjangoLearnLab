from django.urls import path
from .views import BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]

# api_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Ensure this line includes your app's urls.py
]


from django.urls import path, include
from django.http import HttpResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("api.urls")),
    path('', lambda request: HttpResponse('It works!')),
]
