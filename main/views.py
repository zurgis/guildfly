from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post

# Create your views here.
class HomePageView(ListView):
    template_name = 'main/home.html'
    queryset = Post.objects.all()
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'main/postdetail.html'