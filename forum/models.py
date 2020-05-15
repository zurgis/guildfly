from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Forum(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Section(models.Model):
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name


class Topic(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.text