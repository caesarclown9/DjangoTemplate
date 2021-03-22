from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import UserCreationModelForm

User = get_user_model()

class UserRegistrationView(CreateView):
    form_class = UserCreationModelForm
    success_url = reverse_lazy('login')
    template_name = 'registration/registration.html'


class CabinetView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'registration/user_detail.html'


    def get_object(self, queryset=None):
        return self.request.user


