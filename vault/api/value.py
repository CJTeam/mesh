import impl.value as value

def node_add(project, record): 
  print __name__ + ".node_add("+str(record)+","+str(project)+") : [create a node]"
  print "  . fail if 'Label' not provided."
  print "  . fail if 'Label' not unique."
  print "  . generate 'Id'"
  print "  . 'Nodes' value set to 'Label'"
  value.node_add(project, record)

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
