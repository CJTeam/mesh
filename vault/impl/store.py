import os as o
import os.path as p

from util.exit import fail
from util.files import touch

def local_create(name):
  store = "~/mesh"
  _checks(store, name)
  _create(store, name)

def _checks(repos, name):
  git = p.expanduser(repos)
  if not p.isdir(git):
    fail ("store area "+git+" does not exist")
  candidate = p.join(git, name)
  if p.exists(candidate):
    fail ("store "+name+" already exists")

def _create(store, name):
  git = p.expanduser(store)
  project = p.join(git, name)
  o.mkdir(project)
  touch(project, "nodes.csv")
  touch(project, "edges.csv")
