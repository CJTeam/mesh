from system.exit import fail
from util.fields import remainder_of

def check_in_record(k, d):
  if not k in d: fail("'"+k+"' not found in "+str(d))

def check_not_in_record(k, d):
  if k in d: fail("'"+k+"' not found in "+str(d))

def check_not_in_content(k, r, c):
  for v in c:
    if v[k] == r[k]: fail("record with '"+k+'='+r[k]+"' already exists")

def check_no_stragglers(m, ks):
  r = remainder_of(m, ks)
  if r: fail ("spurious keys '"+str(r)+"' in '"+str(m)+"'")

