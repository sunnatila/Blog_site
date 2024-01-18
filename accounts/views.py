from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CustomUserCreateForm


class SignupView(CreateView):
    form_class = CustomUserCreateForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
