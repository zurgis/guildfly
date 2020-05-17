from django.urls import path

from . import views

app_name = 'forum'
urlpatterns = [
    path('', views.ForumListView.as_view(), name='forum'),
    path('<int:forum_id>/', views.SectionListView.as_view(), name='section'),
    path('<int:forum_id>/<int:section_id>/', views.TopicListView.as_view(), name='topic'),
    path('topic/<int:topic_id>/', views.EntryListView.as_view(), name='entry'),
    path('<int:forum_id>/<int:section_id>/create_topic/', views.TopicCreateView.as_view(), name='create_topic'),
    path('<int:section_id>/<int:pk>/update_topic/', views.TopicUpdateView.as_view(), name='update_topic'),
    path('<int:topic_id>/create_entry/', views.EntryCreateView.as_view(), name='create_entry'),
    path('<int:pk>/update_entry/', views.EntryUpdateView.as_view(), name='update_entry'),
    path('<int:pk>/delete_entry/', views.EntryDeleteView.as_view(), name='delete_entry'),
]