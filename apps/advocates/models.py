from enum import unique

from django.db import models


def upload_to(instance, filename):
    return 'advocates/{filename}'.format(filename=filename)

class Advocate(models.Model):
    profile_pic = models.ImageField(upload_to=upload_to, blank=True, null=True)
    username = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    short_bio = models.CharField(max_length=50)
    long_bio = models.TextField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name
