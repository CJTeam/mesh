from django.contrib.auth.models import User
from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    owner = models.ForeignKey(User)
    collaborators = models.ManyToManyField(User, related_name='collaborator_projects')
    node_description = models.CharField(max_length=30)
    edge_description = models.CharField(max_length=30)


class NodeMetadataField(object):
    name = models.CharField(max_length=30)
    sequence_number = models.IntegerField()
    owner = models.ForeignKey(Project)


class EdgeMetadataField(object):
    name = models.CharField(max_length=30)
    sequence_number = models.IntegerField()
    owner = models.ForeignKey(Project)

