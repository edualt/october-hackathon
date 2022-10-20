from django.db import models

from apps.advocates.models import Advocate


def upload_to(instance, filename):
    return 'companies/{filename}'.format(filename=filename)

class Company(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    logo = models.ImageField(upload_to=upload_to, blank=True, null=True)
    href = models.URLField(max_length=200, null=False, blank=False)
    summary = models.TextField()
    advocates = models.ManyToManyField(Advocate, related_name='companies')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name
