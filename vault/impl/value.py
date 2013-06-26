from system.exit import fail
#
def node_add(header, content, record):
    check_in_record("Label", record)
    check_not_in_record("Id", record)
    check_not_in_content("Label", record, content)

    ids = get_all("Id", content)
    nid = next_id(ids)
    print(nid)
    print(record)
    record_add("Id", nid, record)
    print(record)
    check_no_stragglers(record, header)

    raise Exception("NOT IMPLEMENTED 3")

    label = value["Label"]

    check_in_row("Label", value)

    check_unique("Label", value, rows)

    fill_all_empty

# TODO: Move these out to util somewhere
def check_in_record(k, d):
  if not k in d: fail("'"+k+"' not found in "+str(d))

# TODO: extract out dupe w/ check_in_record
def check_not_in_record(k, d):
  if k in d: fail("'"+k+"' not found in "+str(d))

def check_not_in_content(k, r, c):
  for v in c:
    if v[k] == r[k]: fail("record with '"+k+'='+r[k]+"' already exists")

def check_no_stragglers(m, ks):
  r = remainder_of(m, ks)
  if r: fail ("spurious keys '"+str(r)+"' in '"+str(m)+"'")

def get_all(k, d):
  return [v[k] for v in d]

def next_id(ids):
  if not ids: return 1000
  nids = map(int, ids)
  return sorted(nids)[-1] + 1

def record_add(k, v, record):
  if k in record: fail("record should not already have key '"+k+"' value '"+record[k]+"'")
  record[k] = v

def remainder_of(m, ks):
  mks = m.keys()
  return list(set(mks) - set(ks))

#
#  block(attr, data[0])
#
#  print(str(data))
#  raise Exception("NOT IMPLEMENTED")
#
#def block(new, exclude):
#  for v in exclude:
#    if new == v: fail("attribute '"+v+"' already exists '"+str(exclude)+"'")

