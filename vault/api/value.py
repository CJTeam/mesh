def node_create(values): 
  print __name__ + ".node_create("+str(values)+") : [create a node]"
  print "  . fail if 'Label' not provided."
  print "  . fail if 'Label' not unique."
  print "  . generate 'Id'"
  print "  . 'Nodes' value set to 'Label'"
def edge_create(values): 
  print __name__ + ".edge_create("+str(values)+") : [create an edge]"
  print "  . fail if 'Source' not found in nodes."
  print "  . fail if 'Target' not found in nodes."
  print "  . fail if 'Type' not provided."
  print "  . fail if 'Weight' not provided."
  print "  . generate 'Id'"
def node_update(value):
  print __name__ + ".node_update("+str(value)+") : [update a node]"
  print "  . fail if 'Id' not found in nodes."
