import csv
import json

from lxml.builder import E
from lxml import etree

from mesh.models import Edge, Node, EDGE_TYPES


def import_gefx(file, project):
    """
    Import GEFX data into the project.

    """
    parser = etree.XMLParser(ns_clean=True)
    tree = etree.parse(file, parser)
    root = tree.getroot()

    graph_el = root.xpath('//*[local-name() = "graph"]')
    if len(graph_el) == 0:
        return

    graph_el = graph_el[0]
    global_edge_type = graph_el.get('defaultedgetype')

    nodes = {}
    node_els = root.xpath('//*[local-name() = "node"]')
    for node_el in node_els:
        node = Node(name=node_el.get('label'), description=node_el.get('description') or "", project=project)
        node.save()
        nodes[node_el.get('id')] = node

    edge_els = root.xpath('//*[local-name() = "edge"]')
    for edge_el in edge_els:
        edge = Edge(from_node=nodes[edge_el.get('source')], to_node=nodes[edge_el.get('target')], project=project)
        edge_type = edge_el.get('type') or global_edge_type or 'undirected'
        edge.type = 1 if edge_type.lower() == 'undirected' else 2
        edge.save()


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
            id=str(n.name),
            description=n.description,
            label=n.name
        ))

    edges = Edge.objects.filter(project=project)
    edge_els = []
    for e in edges:
        edge_els.append(E.edge(
            id=str(e.id),
            source=str(e.from_node.name),
            target=str(e.to_node.name),
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
