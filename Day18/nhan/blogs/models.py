from django.db import models
from django.db.models.base import Model

# Create your models here.

BLOG_STATUS_CHOICES = (
    ("draft", "Draft"),
    ("published", "Published"),
)

class Blog(models.Model):
    name = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    status = models.CharField(choices=BLOG_STATUS_CHOICES, default="draft", max_length=10)

    def __str__(self):
        return self.namee
    