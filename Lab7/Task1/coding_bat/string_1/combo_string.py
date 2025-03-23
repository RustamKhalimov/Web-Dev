def combo_string(a, b):
  aL = len(a)
  bL = len(b)
  if aL > bL:
    return b+a+b
  else:
    return a+b+a
