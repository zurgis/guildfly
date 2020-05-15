from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, FormView, TemplateView

from .forms import UserRegisterForm, ProfileUpdateForm
from .models import Profile

# Create your views here.
class SignUpPageView(CreateView):
    form_class = UserRegisterForm
    template_name = 'users/signup.html'
    success_url = '/'


class ProfilePageView(TemplateView):
    template_name = 'users/profile.html'


class ProfileUpdateView(FormView):
    form_class = ProfileUpdateForm
    template_name = 'users/profileupdate.html'
    success_url = '/'

    def get_form_kwargs(self):
        user = self.request.user
        form_kwargs = super().get_form_kwargs()
        form_kwargs['user'] = user
        return form_kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)