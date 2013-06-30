from impl.attr import node_create as n_create

def node_create(project, name): 
  n_create(project, name)

def edge_add(project, name): 
  print __name__ + ".edge_add("+project+","+name+") : [create edge attribute]"
  print "  . edge has immutable attributes {Source,Target,Type,Id,Label,Weight}."
  print "  . auto populate all entries with the empty value for this attribute."
  print "  . fail if edge attribute with name '"+name+"' already exists."
