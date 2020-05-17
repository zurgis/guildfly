from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Forum(models.Model):
    name = models.CharField(_('name'), max_length=50)

    def __str__(self):
        return self.name


class Section(models.Model):
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, verbose_name='Форум')
    name = models.CharField(_('name'), max_length=70)

    def __str__(self):
        return self.name


class Topic(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name='Раздел')
    name = models.CharField(_('name'), max_length=100)
    text = models.TextField(_('Text'))
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')

    def __str__(self):
        return self.name


class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name='Тема')
    text = models.TextField(_('Text'))
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.text