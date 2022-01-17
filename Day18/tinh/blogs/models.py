from django.db import models
from django.db.models.enums import Choices
from django.contrib.auth.models import User


# Create your models here.

BLOG_STATUS_CHOICES = (
    ("draft", "Draft"),
    ("published", "Published")
)
class Blog(models.Model):
    name = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    status = models.CharField(choices=BLOG_STATUS_CHOICES, default="draft", max_length=10)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE )
    
    def __str__(self):
        return self.name