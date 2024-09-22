from datetime import datetime

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todo_app.forms import TaskCreationForm, TaskUpdateForm, TagCreationForm
from todo_app.models import Task, Tag


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "todo_app/task_list.html")


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 5
    context_object_name = "tasks_list"
    # template_name = "todo_app/task_list.html"
    queryset = Task.objects.all().prefetch_related("tags__tasks__tags")


# class TaskDetailView(generic.DetailView):
#     model = Task
#     queryset = Task.objects.all().prefetch_related("task__tags")


class TaskCreateView(generic.edit.CreateView):
    model = Task
    form_class = TaskCreationForm
    template_name = "todo_app/task_form.html"


class TaskUpdateView(generic.edit.UpdateView):
    model = Task
    form_class = TaskUpdateForm
    success_url = reverse_lazy("todo_app:index")
    template_name = "todo_app/task_form.html"


class TaskDeleteView(generic.edit.DeleteView):
    model = Task
    success_url = reverse_lazy("todo_app:index")
    template_name = "todo_app/task_confirm_delete.html"


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "todo_app/tag_list.html"
    paginate_by = 2
    queryset = Tag.objects.all()


class TagCreateView(generic.edit.CreateView):
    model = Tag
    form_class = TagCreationForm
    template_name = "todo_app/tag_form.html"


class TagUpdateView(generic.edit.UpdateView):
    model = Tag
    form_class = TagCreationForm
    success_url = reverse_lazy("todo_app:index")


class TagDeleteView(generic.edit.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo_app:index")
