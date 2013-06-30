from impl.loc import nodes
from util.data import load
from system.exit import fail

def node_create(project, attr):
  raise Exception("NOT IMPLEMENTED")
  data = load(nodes(project))

  block(attr, data[0])

  print(str(data))

def block(new, exclude):
  for v in exclude:
    if new == v: fail("attribute '"+v+"' already exists '"+str(exclude)+"'")
