from django.urls import path

from todo_app.views import (
    index,
    TaskListView,
    TaskCreateView,
    TagListView,
    TagCreateView,
    TagDeleteView,
    TaskDeleteView,
    TaskUpdateView
)

urlpatterns = [
    path("", TaskListView.as_view(), name='index'),
    path("tasks/", TaskListView.as_view(), name='tasks-list'),
    path("tasks/create", TaskCreateView.as_view(), name='task-create'),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name='task-update'),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name='task-delete'),
    path("tags/", TagListView.as_view(), name='tags-list'),
    path("tags/create", TagCreateView.as_view(), name='tag-create'),
    path("tags/<int:pk>/update/", TagCreateView.as_view(), name='tag-update'),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name='tag-delete'),
]

app_name = "todo_app"
