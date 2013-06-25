from system.exit import fail
#
def node_add(header, content, record):
    check_in_record("Label", record)
    check_not_in_content("Label", record, content)


    raise Exception("NOT IMPLEMENTED 3")

    label = value["Label"]

    check_in_row("Label", value)

    check_unique("Label", value, rows)

    fill_all_empty

def check_in_record(k, d):
  if not k in d: fail("'"+k+"' not found in "+str(d))

def check_not_in_content(k, r, c):
  for v in c:
    if v[k] == r[k]: fail("record with '"+k+'='+r[k]+"' already exists")
#
#  block(attr, data[0])
#
#  print(str(data))
#  raise Exception("NOT IMPLEMENTED")
#
#def block(new, exclude):
#  for v in exclude:
#    if new == v: fail("attribute '"+v+"' already exists '"+str(exclude)+"'")

