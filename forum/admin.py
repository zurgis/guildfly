from django.contrib import admin

from .models import Forum, Section, Topic, Entry

# Register your models here.
admin.site.register(Forum)
admin.site.register(Section)
admin.site.register(Topic)
admin.site.register(Entry)