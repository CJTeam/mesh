import os.path as p

def store():
  return p.expanduser("~/mesh")

def project(name):
  return p.join(store(), name)

def nodes(name):
  return p.join(project(name), "nodes.csv")

def edges(name):
  return p.join(project(name), "edges.csv")
