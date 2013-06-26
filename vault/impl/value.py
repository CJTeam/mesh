from system.exit import fail

from util.checks import check_in_record
from util.checks import check_not_in_record
from util.checks import check_not_in_content
from util.checks import check_no_stragglers
from util.records import record_add
from util.ids import next_id

def node_add(header, content, record):
    check_in_record("Label", record)
    check_not_in_record("Id", record)
    check_not_in_content("Label", record, content)

    record_add("Id", next_id(content), record)
    print(record)
    check_no_stragglers(record, header)

    raise Exception("NOT IMPLEMENTED 3")

    label = value["Label"]

    check_in_row("Label", value)

    check_unique("Label", value, rows)

    fill_all_empty

#
#  block(attr, data[0])
#
#  print(str(data))
#  raise Exception("NOT IMPLEMENTED")
#
#def block(new, exclude):
#  for v in exclude:
#    if new == v: fail("attribute '"+v+"' already exists '"+str(exclude)+"'")

