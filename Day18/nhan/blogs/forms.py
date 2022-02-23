from django import forms
from .models import BLOG_STATUS_CHOICES
from django.contrib.auth.models import User

class BlogCreationForm(forms.Form):
    name = forms.CharField(max_length=100)
    content = forms.CharField(max_length=1000)
    status = forms.ChoiceField(choices=BLOG_STATUS_CHOICES)
    author = forms.ChoiceField(choices=())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #Get all user
        list_users = User.objects.all()
        AUTHOR_CHOICES = ((user.id, user.username) for user in list_users)

        #Add dynamic users choice
        self.fields['author'].choices = AUTHOR_CHOICES


    