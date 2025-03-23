def common_end(a, b):
  aL = len(a) - 1
  bL = len(b) - 1
  return a[0] == b[0] or a[aL] == b[bL]
