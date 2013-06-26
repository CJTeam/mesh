from util.content import get_all

def next_id(content):
    ids = get_all("Id", content)
    return bump_id(ids)

def bump_id(ids):
  if not ids: return 1000
  nids = map(int, ids)
  return sorted(nids)[-1] + 1
