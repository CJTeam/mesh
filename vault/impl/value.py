from impl.loc import nodes
from util.data import load
from system.exit import fail
#
def node_add(project, record):
    data = load(nodes(project))

    # Ensure required values exist.
    #
    # (Label)
    check_in_record("Label", record)

    # Fail if record already exists.
    #
    # (Label,Id)
    #

    label = value["Label"]

    check_in_row("Label", value)

    check_unique("Label", value, rows)

    fill_all_empty

def check_in_record(k, d):
  if not k in d: fail(k+" not found in "+str(d))
#
#  block(attr, data[0])
#
#  print(str(data))
#  raise Exception("NOT IMPLEMENTED")
#
#def block(new, exclude):
#  for v in exclude:
#    if new == v: fail("attribute '"+v+"' already exists '"+str(exclude)+"'")

