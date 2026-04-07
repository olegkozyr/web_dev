from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Post

# Create your tests here.
class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret',
        )
        cls.title = "New title"
        cls.body = 'Body content'
        cls.author = cls.user
        cls.post = Post.objects.create(
            title=cls.title,
            body=cls.body,
            author=cls.author
        )

    def test_post_model(self):
        self.assertEqual(self.post.title, self.title)
        self.assertEqual(self.post.body, self.body)
        self.assertEqual(self.post.author, self.author)
        self.assertEqual(self.post.get_absolute_url(), '/post/1/')

    def test_url_exists(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_post_listview(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.body)
        self.assertTemplateUsed(response, 'home.html')