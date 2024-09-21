from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Post, Comment

User = get_user_model()

class PostTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_create_post(self):
        response = self.client.post('/api/posts/', {'title': 'New Post', 'content': 'Post content'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_posts(self):
        response = self.client.get('/api/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

# Similar tests can be written for comments

# Create your tests here.
