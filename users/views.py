from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, FormView, TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from .forms import UserRegisterForm, ProfileUpdateForm
from .models import Profile

# Create your views here.
class SignUpPageView(SuccessMessageMixin, CreateView):
    """Страница регистрации пользователя"""
    form_class = UserRegisterForm
    template_name = 'users/signup.html'
    success_message = 'Пользователь %(username)s зарегистрирован!'
    success_url = '/'


class ProfilePageView(TemplateView):
    """Страница профиля"""
    template_name = 'users/profile.html'


class ProfileUpdateView(SuccessMessageMixin, FormView):
    """Страница редактирования профиля"""
    form_class = ProfileUpdateForm
    template_name = 'users/profileupdate.html'
    success_message = 'Ваш профиль был обновлен!'
    success_url = reverse_lazy('users:profile')

    def get_form_kwargs(self):
        # Передаем аргументы в класс формы
        # для последующего сохранения
        user = self.request.user
        form_kwargs = super().get_form_kwargs()
        form_kwargs['user'] = user
        return form_kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)