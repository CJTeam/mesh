def line(f):
  with open(f, 'r') as f:
    top = f.readline()
  return top.strip().split(",")
