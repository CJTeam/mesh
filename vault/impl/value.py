from impl.loc import nodes
from impl.loc import edges
from system.exit import fail
from util.checks import check_in_record
from util.checks import check_not_in_record
from util.checks import check_not_in_content
from util.checks import check_no_stragglers
from util.data import load
from util.data import save
from util.ids import next_id
from util.records import record_add
from util.content import content_add

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
  edge_add_record(edata[0], edata[1], ndata[0], ndata[1], record)
#  fail if 'Source' not found in nodes."
#  fail if 'Target' not found in nodes."
#  fail if 'Type' not provided."
#  fail if 'Weight' not provided."
#  generate 'Id'"
  raise Exception("TO IMPLEMENT ... edge create")
  save(e, edges)


def node_add_record(header, content, record):
    check_in_record("Label", record)
    check_not_in_record("Id", record)
    check_not_in_content("Label", record, content)
    record_add("Id", str(next_id(content)), record)
    content_add(record, content)
    check_no_stragglers(record, header)

def edge_add_record(eheader, econtent, sheader, scontent, record):
    check_in_record("Source", record)
    check_in_record("Target", record)
    check_in_record("Type", record)
    check_in_record("Label", record)
    check_in_record("Weight", record)
