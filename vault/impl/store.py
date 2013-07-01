import os.path as p

from impl.loc import store
from impl.loc import project
from impl.loc import nodes
from impl.loc import edges

from system.files import create
from system.exit import fail
from system.files import mkdir

def local_create(name):
  if not p.isdir(store()):
    fail("store area "+store()+" does not exist")
  if p.exists(project(name)):
    fail("store "+project(name)+" already exists")
  mkdir(project(name))
  create(nodes(name), "Id,Label")
  create(edges(name), "Source,Target,Type,Id,Label,Weight")
