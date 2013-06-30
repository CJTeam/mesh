from itertools import chain
# TODO: Move out
def get_values(k, c):
  return [v[k] for v in c]

def get_records(k, v, c):
  return reduce(lambda a, x: list(chain(a, record_match(k, v, x))), c, [])

def get_record(k, v, c):
  r = get_records(k, v, c)
  if len(r) != 1: fail("expected one record but found multiple with key '"+k+"' and value '"+v+"'")
  return r[0]

# TODO: COMPLETE
def exclude_records(k, v, c):
  raise Exception("COMPLETE ME")

def content_add(record, content):
  content.append(record)

def record_match(k, v, r):
  if k in r and (r[k] == v): return [r]
  else: return []
