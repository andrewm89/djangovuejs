from __future__ import unicode_literals

from django.db import models

# Create your models here.
class JobList(models.Model):
    jobtitle = models.CharField(max_length=100)
    jobdescription = models.TextField(max_length=300)
    postdate = models.DateField(auto_now_add=True)
