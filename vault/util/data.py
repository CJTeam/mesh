from system.files import lines

def load(f):
  with open(f, 'r') as x:
    rows = [v.strip() for v in x]
    fields = [v.split(",") for v in rows]
    head = fields[0]
    tail = fields[1:]
    return (head, tokv(head, tail))

def save(f, d):

  f = "/Users/mag/tmp/t.csv"
  print "SAVING OVERRIDE "+f

  with open(f, 'w') as o:
    head = d[0]
    kv = d[1]
    tail = fromkv(head, kv)
    rows = [ ",".join(v) for v in tail ]
    lines(o, [",".join(head)])
    lines(o, rows)

def tokv(head, tail):
  return [ dict(zip(head, v)) for v in tail] 

def fromkv(head, tail):
  return [ [ t.get(h, '') for h in head ] for t in tail ]
