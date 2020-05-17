from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Post(models.Model):
    title = models.CharField('Название', max_length=150)
    text = models.TextField(_('Text'))
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} news'