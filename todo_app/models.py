from django.db import models
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse("todo_app:tags-list")

    def __str__(self):
        return f"{self.name}"


class Task(models.Model):
    content = models.TextField(max_length=5000)
    datetime = models.DateTimeField(auto_now_add=True)
    сompleted_task = models.BooleanField(default=False, blank=True)
    deadline = models.DateTimeField(
        null=True,
        blank=True,
    )
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE, default=None)

    class Meta:
        verbose_name = "task"
        verbose_name_plural = "tasks"
        ordering = ["datetime", "сompleted_task"]

    def get_absolute_url(self):
        return reverse("todo_app:tasks-list")

    def __str__(self):
        return f"{self.content}, {self.сompleted_task}, {self.datetime}, {self.tags}"
