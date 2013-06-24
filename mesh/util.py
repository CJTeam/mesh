import csv
import json

from mesh.models import Edge, Node

def write_gephi_csv(file, project):
    writer = csv.writer(file)
    edges = Edge.objects.filter(project=project)
    for e in edges:
        writer.writerow([e.from_node.name, e.to_node.name])



def project_graph_json(project):
    nodes = Node.objects.filter(project=project)
    edges = Edge.objects.filter(project=project)
    data = {
        'edges' : [{'id' : e.id, 'description' : e.description, 'sourceNode' : e.from_node.name, 'targetNode' : e.to_node.name, 'type' : e.type} for e in edges],
        'nodes' : [{'id' : n.name, 'description' : n.description} for n in nodes]
    }
    return json.dumps(data)
