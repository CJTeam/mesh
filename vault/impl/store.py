import os as o
import os.path as p

from util.exit import fail
from util.files import touch
from util.files import create

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
  create(project, "nodes.csv", "Id,Label")
  create(project, "edges.csv", "Source,Target,Type,Id,Label,Weight")
