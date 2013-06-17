from django.contrib.auth.models import User
from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    owner = models.ForeignKey(User)
    collaborators = models.ManyToManyField(User, related_name='collaborator_projects')