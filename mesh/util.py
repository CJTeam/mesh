import csv
import json

from lxml.builder import E
from lxml import etree

from mesh.models import Edge, Node, EDGE_TYPES

def write_gephi_csv(file, project):
    """
    Generate very simple CSV file for the project.

    """
    writer = csv.writer(file)
    edges = Edge.objects.filter(project=project)
    for e in edges:
        writer.writerow([e.from_node.name, e.to_node.name])


def write_gexf(file, project):
    """
    Generate a GEXF file for the project.

    """
    nodes = Node.objects.filter(project=project)
    node_els = []
    for n in nodes:
        node_els.append(E.node(
            id=str(n.id),
            description=n.description,
            label=n.name
        ))

    edges = Edge.objects.filter(project=project)
    edge_els = []
    for e in edges:
        edge_els.append(E.edge(
            id=str(e.id),
            source=str(e.from_node.id),
            target=str(e.to_node.id),
            type='undirected' if e.type == 1 else 'directed'
        ))

    root = E.gexf(
        E.graph(
            E.nodes(*node_els),
            E.edges(*edge_els)
        )
    )

    file.write(etree.tostring(root))


def project_graph_json(project):
    """
    Generate JSON data for visualising a project graph.

    """
    nodes = Node.objects.filter(project=project)
    edges = Edge.objects.filter(project=project)
    data = {
        'edges' : [{'id' : e.id, 'description' : e.description, 'sourceNode' : e.from_node.name, 'targetNode' : e.to_node.name, 'type' : e.type} for e in edges],
        'nodes' : [{'id' : n.name, 'description' : n.description} for n in nodes]
    }
    return json.dumps(data)
