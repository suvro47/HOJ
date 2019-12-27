from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from problems.models import Problem


class Submission(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.SET_DEFAULT)
    problem = models.ForeignKey(Problem, default=1, on_delete=models.SET_DEFAULT)
    language = models.CharField(max_length=100, null=True)
    solution = models.FileField()
    consumed_time = models.IntegerField(null=True)
    consumed_memory = models.IntegerField(null=True)
    submission_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.pk


