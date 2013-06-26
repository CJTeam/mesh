from impl.loc import nodes
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

def node_add(project, record):
  n = nodes(project)
  data = load(n)
  print(record)
  node_add_content(data[0], data[1], record)
  print(record)
  save(n, data)

def node_add_content(header, content, record):
    check_in_record("Label", record)
    check_not_in_record("Id", record)
    check_not_in_content("Label", record, content)
    record_add("Id", str(next_id(content)), record)
    content_add(record, content)
    check_no_stragglers(record, header)
