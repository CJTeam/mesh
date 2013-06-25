import os
import os.path as path

def mkdir(d):
  os.mkdir(d)

def create(f, c):
  with open(f, 'w') as s:
    s.write(c+"\n")
