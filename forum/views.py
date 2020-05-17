from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.exceptions import Http404
from django.http import HttpResponseRedirect

from .models import Forum, Section, Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.
class ForumListView(ListView):
    """Страница с форумом"""
    model = Forum
    template_name = 'forum/forum.html'


class SectionListView(ListView):
    """Страница разделов"""
    paginate_by = 3
    template_name = 'forum/section.html'
    
    def get_queryset(self):
        # Выводим разделы принадлежащие определенному форуму
        self.forum = get_object_or_404(Forum, id=self.kwargs['forum_id'])
        return Section.objects.filter(forum=self.forum)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['forum'] = self.forum
        return context


class TopicListView(ListView):
    """Страница тем"""
    paginate_by = 3
    template_name = 'forum/topic.html'

    def get_queryset(self):
        # Выводим разделы принадлежащие определенному форуму
        self.forum = get_object_or_404(Forum, id=self.kwargs['forum_id'])
        self.section = get_object_or_404(Section, id=self.kwargs['section_id'])
        return Topic.objects.filter(section=self.section)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['forum'] = self.forum
        context['section'] = self.section
        return context


class EntryListView(ListView):
    """Страница записей"""
    paginate_by = 3
    template_name = 'forum/entry.html'
    
    def get_queryset(self):
        # Выводим разделы принадлежащие определенному форуму
        self.topic = get_object_or_404(Topic, id=self.kwargs['topic_id'])
        return Entry.objects.filter(topic=self.topic)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['topic'] = self.topic
        return context


class TopicCreateView(LoginRequiredMixin, CreateView):
    """Страница создания тем"""
    form_class = TopicForm
    template_name = 'forum/topic_form.html'

    def form_valid(self, form):
        # Переопределяем метод, чтобы назначить раздел и автора
        section = get_object_or_404(Section, id=self.kwargs['section_id'])
        form.instance.section = section
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = get_object_or_404(Section, id=self.kwargs['section_id'])
        return context

    def get_success_url(self):
        return reverse('forum:topic', kwargs={'forum_id': self.kwargs['forum_id'], 
            'section_id': self.kwargs['section_id']})


class TopicUpdateView(LoginRequiredMixin, UpdateView):
    """Страница редактирования тем"""
    model = Topic
    form_class = TopicForm
    template_name = 'forum/topic_update.html'

    def dispatch(self, request, *args, **kwargs):
        # Переопределяем метод, чтобы редактировать мог только автор
        topic = self.get_object()
        if topic.author != request.user:
            raise Http404
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = get_object_or_404(Section, id=self.kwargs['section_id'])
        return context

    def get_success_url(self):
        return reverse('forum:entry', kwargs={'topic_id': self.object.id})


class EntryCreateView(LoginRequiredMixin, CreateView):
    """Страница создания записей"""
    form_class = EntryForm
    template_name = 'forum/entry_form.html'

    def form_valid(self, form):
        # Переопределяем метод, чтобы назначить тему и автора
        topic = get_object_or_404(Topic, id=self.kwargs['topic_id'])
        form.instance.topic = topic
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['topic'] = get_object_or_404(Topic, id=self.kwargs['topic_id'])
        return context

    def get_success_url(self):
        return reverse('forum:entry', kwargs={'topic_id': self.kwargs['topic_id']})


class EntryUpdateView(LoginRequiredMixin, UpdateView):
    """Страница редактирования записей"""
    model = Entry
    form_class = EntryForm
    template_name = 'forum/entry_update.html'

    def dispatch(self, request, *args, **kwargs):
        # Переопределяем метод, чтобы редактировать мог только автор
        self.entry = self.get_object()
        if self.entry.author != request.user:
            raise Http404
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['topic'] = self.entry.topic
        return context
    
    def get_success_url(self):
        return reverse('forum:entry', kwargs={'topic_id': self.entry.topic.id})


class EntryDeleteView(LoginRequiredMixin, DeleteView):
    """Удаляет запись"""
    model = Entry

    def dispatch(self, request, *args, **kwargs):
        # Переопределяем метод, чтобы редактировать мог только автор
        # и убрать подтверждение удаления
        self.entry = self.get_object()
        if self.entry.author != request.user:
            raise Http404
        self.entry.delete()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('forum:entry', kwargs={'topic_id': self.entry.topic.id})