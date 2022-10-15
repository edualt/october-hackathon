from django.db import models

from apps.companies.models import Company


class Advocate(models.Model):
    name = models.CharField(max_length=100)
    # profile_pic = models.ImageField(upload_to='advocates/')
    short_bio = models.CharField(max_length=100)
    long_bio = models.TextField()
    years_of_experience = models.IntegerField()
    company = models.ForeignKey(Company, related_name='advocates', on_delete=models.CASCADE, null=True, blank=True)
    links = models.JSONField(default=dict, blank=True, null=True)

    def __str__(self):
        return self.name
