from impl.value import node_create as n_create
from impl.value import edge_create as e_create
from impl.value import node_delete as n_delete
from impl.value import edge_delete as e_delete

def node_create(project, record): 
  n_create(project, record)

def edge_create(project, record): 
  e_create(project, record)

def node_update(value):
  print __name__ + ".node_update("+str(value)+") : [update a node]"
  print "  . fail if 'Id' not found in nodes."

# edge_update
# node_delete
def node_delete(project, label):
  n_delete(project, label)

def edge_delete(project, source, target):
  e_delete(project, source, target)

# edge_delete

