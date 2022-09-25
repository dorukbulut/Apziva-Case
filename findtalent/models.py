from django.db import models
from django.contrib.postgres.fields import ArrayField
from pkg_resources import compatible_platforms
# Create your models here.


class Individual(models.Model) : 
    name = models.CharField(max_length=64)
    email  = models.EmailField()
    location = models.CharField(max_length=10000)
    bio = models.CharField(max_length=10000)
    job_title = models.CharField(max_length=100)
    skills = models.CharField(max_length=10000)
    github_url = models.CharField(max_length=1000)