from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Todo(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title")
    memo = models.TextField(blank=True, verbose_name="Memo")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Time Created")
    date_completed = models.DateTimeField(null=True, blank=True, verbose_name="Time Completed")
    important = models.BooleanField(default=False, verbose_name="Important")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Owner Name")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'To Do Task'
        verbose_name_plural = 'To Do Tasks'
        ordering = ['-created']
