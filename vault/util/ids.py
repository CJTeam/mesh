from util.content import get_values

def next_id(content):
    ids = get_values("Id", content)
    return bump_id(ids)

def bump_id(ids):
  if not ids: return 1000
  nids = map(int, ids)
  return sorted(nids)[-1] + 1
