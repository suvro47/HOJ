from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField


def upload_path_handler(instance, filename):
    return "datasets/problem{id}/{filename}".format(id=instance.pk, filename=filename)


class Problem(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = RichTextField()
    author = models.CharField(max_length=100, null=True)
    tester = models.CharField(max_length=100, null=True)
    editorial = models.TextField()
    tags = models.CharField(max_length=100, null=True)
    difficulty = models.CharField(max_length=100, null=True)
    time_limit = models.IntegerField(null=True)
    memory_limit = models.IntegerField(null=True)
    permitted_languages = models.CharField(max_length=100, null=True)
    judge_input = models.FileField(upload_to=upload_path_handler)
    judge_output = models.FileField(upload_to=upload_path_handler)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


def save(self, *args, **kwargs):
    if self.id is None:
        saved = []
        for f in self.__class__._meta.get_fields():
            if isinstance(f, models.FileField):
                saved.append((f.name, getattr(self, f.name)))
                setattr(self, f.name, None)

        super(self.__class__, self).save(*args, **kwargs)

        for name, val in saved:
            setattr(self, name, val)
    super(self.__class__, self).save(*args, **kwargs)

