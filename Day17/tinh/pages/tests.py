
from django.urls import reverse
from django.test import TestCase

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