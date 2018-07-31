# Create your models here.
from django.db import models


class ProjectInfo(models.Model):
    projectId = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    projectName = models.CharField(max_length=30)

    def __str__(self):
        return self.projectId + ", " + self.location + ", " + self.projectName
