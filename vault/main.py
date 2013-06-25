import sys
import api.store as store
import api.attr as attr
import api.value as value

sys.dont_write_bytecode = True

# G20

# Meant to mimic a group session.

# Create a project backed by the specified GitHub repository.
# Susan is a member of mesh and also has a GitHub account.
# store.backed_create("https://github.com/susan/g20_summit.git")
store.local_create("g20_summit")

# Add 'Country' attribute to the Node table.
attr.node_create("g20_summit", "Country")

# Add 'Relationship' attribute to the Edge table.
attr.edge_create("Relationship")

# Build Nodes.
value.node_create((("Label","Obama"),("Country","US")))
value.node_create((("Label","Gillard")))
value.node_create((("Label","Merkel"),("Country","DE")))
value.node_create((("Label","Ayrault"),("Country","FR")))
value.node_create((("Label","Cameron"),("Country","UK")))
value.node_create((("Label","Abdullah"),("Country","SA")))

# Build Edges
value.edge_create((("Source","Obama"),("Target","Gillard"),("Type","Directed"),("Label","US-AU"),("Weight",10),("Relationship","Cordial")))
value.edge_create((("Source","Obama"),("Target","Cameron"),("Type","Directed"),("Label","US-UK"),("Weight",50),("Relationship","Friendly")))
value.edge_create((("Source","Gillard"),("Target","Obama"),("Type","Directed"),("Label","AU-US"),("Weight",50),("Relationship","Friendly")))
value.edge_create((("Source","Gillard"),("Target","Cameron"),("Type","Directed"),("Label","AU-UK"),("Weight",30),("Relationship","Close")))
value.edge_create((("Source","Cameron"),("Target","Obama"),("Type","Directed"),("Label","UK-US"),("Weight",50),("Relationship","Close")))
value.edge_create((("Source","Cameron"),("Target","Gillard"),("Type","Directed"),("Label","UK-AU"),("Weight",30),("Relationship","Friendly")))

#
value.node_update((("Label","Gillard"),("Country","AU")))
