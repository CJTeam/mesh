from impl.value import node_create as create

def node_create(project, record): 
  create(project, record)

def edge_add(values): 
  print __name__ + ".edge_create("+str(values)+") : [create an edge]"
  print "  . fail if 'Source' not found in nodes."
  print "  . fail if 'Target' not found in nodes."
  print "  . fail if 'Type' not provided."
  print "  . fail if 'Weight' not provided."
  print "  . generate 'Id'"

def node_update(value):
  print __name__ + ".node_update("+str(value)+") : [update a node]"
  print "  . fail if 'Id' not found in nodes."

# edge_update
# node_delete
# edge_delete
