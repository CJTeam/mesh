from itertools import chain
from system.exit import fail

# TODO: Move out
def get_values(k, c):
  return [v[k] for v in c]

def get_records(k, v, c):
  return reduce(lambda a, x: list(chain(a, [x] if record_match(k, v, x) else [])), c, [])

# TODO: COMPLETE
def exclude_records(k, v, c):
  return reduce(lambda a, x: list(chain(a, [] if record_match(k, v, x) else [x])), c, [])

def get_record(k, v, c):
  r = get_records(k, v, c)
  if len(r) == 0: fail("no record found with key '"+k+"' and value '"+v+"'")
  if len(r) >  1: fail("expected one record but found multiple with key '"+k+"' and value '"+v+"'")
  return r[0]

def record_match(k, v, r):
  if k in r and (r[k] == v): return True
  else: return False  
