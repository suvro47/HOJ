from django.db import models
from user.models import CustomUser
from django.contrib.postgres.fields import ArrayField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone


class Contest(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False)
    category = models.CharField(max_length=100, blank=False)  # team contest or individual contest
    description = models.CharField(max_length=100, blank=False)
    participated_user = ArrayField(models.IntegerField())  # logged user_ids
    no_of_problem = models.IntegerField(default=0)
    problem_list = ArrayField(models.IntegerField()) # problems_ids  
    is_solved = ArrayField(ArrayField(models.BooleanField(default=False)))  # a specific problem is solved by a specific user or not..?
    incorrect_attempt = ArrayField(ArrayField(models.IntegerField(default=0))) # how many times an user (wrong)attempt a specific problem ?
    solved = ArrayField(models.IntegerField(default=0))  #  total solved by a specific user
    penalty = ArrayField(models.IntegerField(default=0))  #  total penalty for a specific user
    start_time = models.DateTimeField(null=True) 
    end_time = models.DateTimeField(null=True)
    
   
    def __str__(self):
        return str(self.id) + '. ' + self.title




