from django.contrib.auth.models import User
from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    owner = models.ForeignKey(User)
    collaborators = models.ManyToManyField(User, related_name='collaborator_projects')
    node_description = models.CharField(max_length=30)
    edge_description = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class NodeMetadataField(models.Model):
    name = models.CharField(max_length=30)
    sequence_number = models.IntegerField()
    owner = models.ForeignKey(Project)


class EdgeMetadataField(models.Model):
    name = models.CharField(max_length=30, unique=True)
    sequence_number = models.IntegerField()
    owner = models.ForeignKey(Project)


class Node(models.Model):
    name = models.CharField(max_length=155)
    description = models.CharField(max_length=200, blank=True)
    project = models.ForeignKey(Project)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


EDGE_TYPES = (
    (1, 'Undirected'),
    (2, 'Directed'),
)


class Edge(models.Model):
    description = models.CharField(max_length=200, blank=True)
    from_node = models.ForeignKey(Node, related_name='from_edges')
    to_node = models.ForeignKey(Node, related_name='to_edges')
    type = models.IntegerField(choices=EDGE_TYPES)
    project = models.ForeignKey(Project)

    def __str__(self):
        if self.type == 1:
            return '{} - {}'.format(self.from_node.name, self.to_node.name)
        return '{} > {}'.format(self.from_node.name, self.to_node.name)
