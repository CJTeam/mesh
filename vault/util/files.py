import os.path as path

def touch(p, f):
  n = path.join(p, f)
  open(n, 'a').close()

def create(p, f, c):
  n = path.join(p, f)
  with open(n, 'w') as s:
    s.write(c+"\n")
