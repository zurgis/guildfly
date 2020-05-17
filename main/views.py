from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post

# Create your views here.
class HomePageView(ListView):
    """Главная страница"""   
    model = Post
    ordering = '-date_added'
    paginate_by = 2
    template_name = 'main/home.html'

class PostDetailView(DetailView):
    """Страница новости"""
    model = Post
    template_name = 'main/postdetail.html'