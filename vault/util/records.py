from system.exit import fail

def record_add(k, v, record):
  if k in record: fail("record should not already have key '"+k+"' value '"+record[k]+"'")
  record[k] = v
