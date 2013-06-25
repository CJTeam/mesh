import os.path as p

from util.exit import fail

repos = "~/mesh"

def local_create(name):
  if not p.isdir(repos):
    fail ("repository area "+repos+" does not exist")
  candidate = p.join(repos, name)
  if p.exists(candidate):
    fail ("repository "+name+" already exists")
