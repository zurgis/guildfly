from django.urls import path

from . import views

app_name = 'forum'
urlpatterns = [
    path('', views.ForumListView.as_view(), name='forum'),
    path('<int:forum_id>/', views.SectionListView.as_view(), name='section'),
]