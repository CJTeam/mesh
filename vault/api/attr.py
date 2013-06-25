import impl.attr as attr

def node_create(name): 
  print __name__ + ".node_create("+name+") : [create node attribute]"
  print "  . node table has immutable attributes {Nodes,Id,Label}."
  print "  . auto populate all entries with the empty value for this attribute."
  print "  . fail if node attribute with name '"+name+"' already exists."
  attr.node_create(name)

def edge_create(name): 
  print __name__ + ".edge_create("+name+") : [create edge attribute]"
  print "  . edge has immutable attributes {Source,Target,Type,Id,Label,Weight}."
  print "  . auto populate all entries with the empty value for this attribute."
  print "  . fail if edge attribute with name '"+name+"' already exists."
