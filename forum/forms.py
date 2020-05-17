from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    """Форма для тем"""
    class Meta:
        model = Topic
        fields = ['name', 'text']
        labels = {'name': 'Название темы:', 'text': 'Текст:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}


class EntryForm(forms.ModelForm):
    """Форма для записей"""
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Текст:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}