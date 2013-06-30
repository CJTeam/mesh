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

# Create a node
value.node_create("g20_summit", {"Label": "Obama"})

# Create an edge 
value.edge_create("g20_summit", {"Source": "Obama", "Target": "Obama", "Type": "Undirected", "Label": "US-US", "Weight": "0"})

# Add 'Country' attribute to the node table
attr.node_create("g20_summit", "Country")

# Add 'Relationship' attribute to the edge table
attr.edge_create("g20_summit", "Relationship")

# Build nodes
value.node_create("g20_summit", {"Label": "Gillard" , "Country": "AU"})
value.node_create("g20_summit", {"Label": "Merkel"  , "Country": "DE"})
value.node_create("g20_summit", {"Label": "Ayrault" , "Country": "FR"})
value.node_create("g20_summit", {"Label": "Cameron" , "Country": "UK"})
value.node_create("g20_summit", {"Label": "Abdullah", "Country": "SA"})

# Build edges
value.edge_create("g20_summit", {"Source": "Gillard", "Target": "Gillard", "Type": "Undirected", "Label": "AU-AU", "Weight": "0", "Relationship": "Self"})
value.edge_create("g20_summit", {"Source": "Merkel", "Target": "Merkel", "Type": "Undirected", "Label": "DE-DE", "Weight": "0", "Relationship": "Self"})
value.edge_create("g20_summit", {"Source": "Ayrault", "Target": "Ayrault", "Type": "Undirected", "Label": "FR-FR", "Weight": "0", "Relationship": "Self"})
value.edge_create("g20_summit", {"Source": "Cameron", "Target": "Cameron", "Type": "Undirected", "Label": "UK-UK", "Weight": "0", "Relationship": "Self"})
value.edge_create("g20_summit", {"Source": "Abdullah", "Target": "Abdullah", "Type": "Undirected", "Label": "SA-SA", "Weight": "0", "Relationship": "Self"})

raise Exception("NOT IMPLEMENTED main")

value.node_update("g20_summit", {"Label": "Obama", "Country": "US"})
value.edge_update("g20_summit", {"Source": "Obama", "Target": "Obama", "Type": "Undirected", "Label": "US-US", "Weight": "0", "Relationship": "Self"})

# Build Edges
value.edge_create((("Source","Obama"),("Target","Gillard"),("Type","Directed"),("Label","US-AU"),("Weight",10),("Relationship","Cordial")))
value.edge_create((("Source","Obama"),("Target","Cameron"),("Type","Directed"),("Label","US-UK"),("Weight",50),("Relationship","Friendly")))
value.edge_create((("Source","Gillard"),("Target","Obama"),("Type","Directed"),("Label","AU-US"),("Weight",50),("Relationship","Friendly")))
value.edge_create((("Source","Gillard"),("Target","Cameron"),("Type","Directed"),("Label","AU-UK"),("Weight",30),("Relationship","Close")))
value.edge_create((("Source","Cameron"),("Target","Obama"),("Type","Directed"),("Label","UK-US"),("Weight",50),("Relationship","Close")))
value.edge_create((("Source","Cameron"),("Target","Gillard"),("Type","Directed"),("Label","UK-AU"),("Weight",30),("Relationship","Friendly")))

#
value.node_update((("Label","Gillard"),("Country","AU")))



# TODO: Disallow "," in any values.
