from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'users'
urlpatterns = [
    path('signup/', views.SignUpPageView.as_view(), name='signup'),
    path('profile/', views.ProfilePageView.as_view(), name='profile'),
    path('update/', views.ProfileUpdateView.as_view(), name='profileupdate'),
]