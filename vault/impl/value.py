from impl.loc import nodes
from impl.loc import edges
from system.exit import fail
from util.checks import check_in_record
from util.checks import check_not_in_record
from util.checks import check_in_content
from util.checks import check_not_in_content
from util.checks import check_no_stragglers
from util.data import load
from util.data import save
from util.ids import next_id
from util.records import record_add
from util.content import get_record

def node_create(project, record):
  n = nodes(project)
  data = load(n)
  node_add_record(data[0], data[1], record)
  save(n, data)

def edge_create(project, record):
  e = edges(project)
  n = nodes(project)
  edata = load(e)
  ndata = load(n)
  edge_add_record(ndata[0], ndata[1], edata[0], edata[1], record)
  save(e, edata)

def node_delete(project, label):
  e = edges(project)
  n = nodes(project)
  edata = load(e)
  ndata = load(n)
  node_del_record(ndata[0], ndata[1], edata[0], edata[1], label)
  save(n, ndata)

def node_add_record(header, content, record):
    check_in_record("Label", record)
    check_not_in_record("Id", record)
    check_not_in_content("node", "Label", record["Label"], content)
    record_add("Id", str(next_id(content)), record)
    content.append(record)
    check_no_stragglers(record, header)

def edge_add_record(nheader, ncontent, eheader, econtent, record):
    check_in_record("Source", record)
    check_in_record("Target", record)
    check_in_record("Type", record)
    check_in_record("Label", record)
    check_in_record("Weight", record)
    check_in_content("node", "Label", record["Source"], ncontent)
    check_in_content("node", "Label", record["Target"], ncontent)
    econtent.append(record)
    check_no_stragglers(record, eheader)

def node_del_record(nheader, ncontent, eheader, econtent, label):
    record = get_record("Label", label, ncontent) 
    check_in_record("Label", record)
    check_not_in_content("edge", "Source", label, econtent)
    check_not_in_content("edge", "Target", label, econtent)
    ncontent.remove(record)
