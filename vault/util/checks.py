from system.exit import fail
from util.fields import remainder_of

def check_in_record(k, d):
  if not k in d: fail("'"+k+"' not found in "+str(d))

def check_not_in_record(k, d):
  if k in d: fail("'"+k+"' not found in "+str(d))

def check_in_content(m, k, v, c):
  if in_content(k, v, c): fail(m+" with '"+k+'='+v+"' does not exist")

def check_not_in_content(m, k, v, c):
  if not in_content(k, v, c): fail(m+" with '"+k+'='+v+"' exists")

def in_content(k, v, c):
  return not reduce(lambda a, x: a or map_val_eq(k, v, x), c, False)

def check_no_stragglers(m, ks):
  r = remainder_of(m, ks)
  if r: fail ("spurious keys '"+str(r)+"' in '"+str(m)+"'")

def map_val_eq(k, v, m):
  return k in m and (m[k] == v)
