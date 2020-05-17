from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _

class UserRegisterForm(UserCreationForm):
    """Форма регистрации"""
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileUpdateForm(forms.Form):
    """Форма обновления профиля"""
    email = forms.EmailField(label=_('Email address'))
    image = forms.ImageField(label=_('Image'))

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

        self.user = user
        self.profile = user.profile
        # Передаем полям определенные значения
        self.fields['email'].initial = user.email
        self.fields['image'].initial = self.profile.image
    
    def save(self):
        # Переопределяем метод save, чтобы сохранить
        # одновременно значения в разных таблицах
        user = self.user
        user.email = self.cleaned_data['email']
        profile = self.profile
        profile.image = self.cleaned_data['image']
        user.save()
        profile.save()