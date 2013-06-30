from impl.value import node_create as n_create
from impl.value import edge_create as e_create
from impl.value import node_update as n_update
from impl.value import edge_update as e_update
from impl.value import node_delete as n_delete
from impl.value import edge_delete as e_delete

def node_create(project, record): 
  n_create(project, record)

def edge_create(project, record): 
  e_create(project, record)

def node_update(project, record):
  n_update(project, record)

def edge_update(project, record):
  e_update(project, record)

def node_delete(project, label):
  n_delete(project, label)

def edge_delete(project, source, target):
  e_delete(project, source, target)
