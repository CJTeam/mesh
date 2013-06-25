from impl.loc import nodes
from util.data import load
from system.exit import fail

def node_add(project, attr):
  data = load(nodes(project))

  block(attr, data[0])

  print(str(data))
  raise Exception("NOT IMPLEMENTED")

def block(new, exclude):
  for v in exclude:
    if new == v: fail("attribute '"+v+"' already exists '"+str(exclude)+"'")
