from django.db import models
from django.contrib.postgres.fields import ArrayField
from ckeditor_uploader.fields import RichTextUploadingField

class Contest(models.Model):
    title = models.CharField(max_length=100, blank=False)
    difficulty = models.CharField(max_length=100)
    no_of_problems = models.IntegerField(default=0)
    no_of_submissions = models.IntegerField(default=0)
    no_of_accepted = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id) + '. ' + self.title
