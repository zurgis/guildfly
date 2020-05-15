from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileUpdateForm(forms.Form):
    email = forms.EmailField()
    image = forms.ImageField()

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

        self.user = user
        self.profile = user.profile
        self.fields['email'].initial = user.email
        self.fields['image'].initial = self.profile.image
    
    def save(self):
        user = self.user
        user.email = self.cleaned_data['email']
        profile = self.profile
        profile.image = self.cleaned_data['image']
        user.save()
        profile.save()