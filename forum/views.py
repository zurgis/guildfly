from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Forum, Section

# Create your views here.
class ForumListView(ListView):
    model = Forum
    template_name = 'forum/forum.html'


class SectionListView(ListView):
    context_object_name = 'sections'
    template_name = 'forum/section.html'
    
    def get_queryset(self):
        self.forum_id = get_object_or_404(Forum, id=self.kwargs['forum_id'])
        return Section.objects.filter(forum_id=self.forum_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['forum_id'] = self.forum_id
        return context