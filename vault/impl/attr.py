from impl.loc import nodes
from impl.loc import edges
from util.data import load
from util.data import save
from system.exit import fail

def node_create(project, attr):
  create("node", nodes(project), attr)

def edge_create(project, attr):
  create("edge", edges(project), attr)

def create(which, f, attr):
  data = load(f)
  create_it(which, data[0], attr)
  save(f, data)

def create_it(which, header, attr):
  if attr in header: fail(which+" attribute '"+attr+"' already exists "+str(header))
  header.append(attr) 
