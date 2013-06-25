import os.path as p

from loc import store
from loc import project
from loc import nodes
from loc import edges

from util.exit import fail
from util.files import create
from util.files import mkdir

def local_create(name):
  if not p.isdir(store()):
    fail ("store area "+store()+" does not exist")
  if p.exists(project(name)):
    fail ("store "+project(name)+" already exists")
  mkdir(project(name))
  create(nodes(name), "Id,Label")
  create(edges(name), "Source,Target,Type,Id,Label,Weight")
