from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Step(models.Model):
    step = models.CharField(max_length=200, default="")
    step_desc = models.CharField(max_length=300, default="")
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return "* {}".format(self.step)


class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    task = models.CharField(max_length=200, default="")
    steps = models.ManyToManyField(Step)
    owner = models.ForeignKey('auth.user', related_name='tasks', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
    seg = [
        ("Today", "My Day"),
        ("Imp", "Important"),
        ("Planned", "Planned"),
        ("Assigned", "Assigned To Me"),
        ("Flagged", "Flagged Email"),
    ]
    segment = models.CharField(max_length=20, choices=seg, default="Today")

    def __str__(self):
        return "{}. {} - {}".format(self.task_id, self.task, self.owner)

    def get_absolute_url(self):
        return reverse('Task_Details', kwargs={'pk': self.task_id})

