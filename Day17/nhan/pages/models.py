from django.db import models

# Create your models here.

BLOG_STATUS_CHOICES = (
    ("draft", "Draft"),
    ("published", "Published"),
)

class Blog(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(choices=BLOG_STATUS_CHOICES, default="draft", max_length=10)
    description = models.CharField(max_length=100, default="")