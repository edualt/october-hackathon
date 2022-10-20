from django.db import models

from apps.advocates.models import Advocate


class Link(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    advocate = models.ForeignKey(Advocate, related_name='links', on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name
