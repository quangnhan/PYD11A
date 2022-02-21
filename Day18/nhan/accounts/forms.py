import re
from django import forms
# from django.contrib.auth.models import User


class UserCreationForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean_password(self):
        password = self.cleaned_data['password']

        # calculating the length
        if len(password) < 8:
            raise forms.ValidationError("Use at least 8 characters")

        return password