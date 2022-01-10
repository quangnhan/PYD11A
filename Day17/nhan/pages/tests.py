from django.urls import reverse
from django.test import TestCase
from .models import Blog

# Create your tests here.

class HomePageTest(TestCase):
    def test_home_page(self):
        url = reverse("home")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

class AboutPageTest(TestCase):
    def test_about_page(self):
        url = reverse("about")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

class BlogModelTest(TestCase):
    def test_create_blog(self):
        blog = Blog.objects.create(name="Blog 1")
        self.assertEqual(blog.name, "Blog 1")
        self.assertEqual(blog.status, "draft")


