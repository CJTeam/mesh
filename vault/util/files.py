import os.path as path

def touch(p, f):
  n = path.join(p, f)
  open(n, 'a').close()
