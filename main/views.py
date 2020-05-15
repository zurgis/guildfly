from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post

# Create your views here.
class HomePageView(ListView):   
    model = Post
    paginate_by = 1
    template_name = 'main/home.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'main/postdetail.html'