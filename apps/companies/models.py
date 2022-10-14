from email.policy import default

from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    # logo = models.ImageField(upload_to='companies/')
    href = models.URLField(max_length=200, null=False, blank=False)
    summary = models.TextField()

    def __str__(self):
        return self.name
