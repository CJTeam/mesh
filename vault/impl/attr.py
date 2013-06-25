#import os as o
#import os.path as p

#from util.exit import fail
#from util.files import touch
#from util.files import create

from loc import nodes
import util.top as top

def node_create(project, attr):
  cs = top.line(nodes(project))
  print ("first line "+str(cs))
  raise Exception("continue")
