# accounts/views.py
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

class SignUpView(FormView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']

        # Create new user
        # get_user_model().objects.create_user(username=email, email=email, password=password)
        User.objects.create_user(username=email, email=email, password=password)

        return super().form_valid(form)