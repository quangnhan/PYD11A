import re
from django import forms
from django.contrib.auth.models import User


class UserCreationForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean_email(self):
        email = self.cleaned_data['email']

        if len(User.objects.filter(email=email)) > 0:
            raise forms.ValidationError("Email is exist")

        return email

    def clean_password(self):
        password = self.cleaned_data['password']

        # calculating the length
        if len(password) < 8:
            raise forms.ValidationError("Use at least 8 characters")

        # searching for digits
        if re.search(r"\d", password) is None:
            raise forms.ValidationError("Use at least 1 number")

        # searching for uppercase and searching for lowercase
        if re.search(r"[A-Z]", password) is None or re.search(r"[a-z]", password) is None:
            raise forms.ValidationError("Use a mix of upper and lower case characters")

        # searching for symbols
        if re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~"+r'"]', password) is None:
            raise forms.ValidationError("Use at least 1 special character like “.”, “&”, or “*”")

        return password