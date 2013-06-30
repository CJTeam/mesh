from impl.loc import nodes
from util.data import load
from util.data import save
from system.exit import fail

def node_create(project, attr):
  n = nodes(project)
  data = load(n)
  node_add_attr(data[0], attr)
  save(n, data)

def node_add_attr(header, attr):
  if attr in header: fail("node attribute '"+attr+"' already exists "+str(header))
  header.append(attr) 
