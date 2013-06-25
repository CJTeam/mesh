import impl.store as store

def local_create(name):
  print __name__ + ".local_create("+name+") : [create project backed by local repository only]"
  print "  . "+"ensure "+name+" does not already exist within mesh."
  print "  . "+"create and initialise local git repi in mesh project area."
  store.local_create(name)

def backed_create(url):
  print __name__ + ".backed_create("+url+") : [create project backed by github repository]"
  print "  . "+"ensure name portion of git repo does not already exist within mesh."
  print "  . "+"clone "+url+" to mesh project area."
