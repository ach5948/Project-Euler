def total(filename):
  names = []

  with open(filename) as fopen:
    names = fopen.readline().lower().split(',')
    names.sort()
  
  val = 0
  start = ord('a') - 1

  for i in range(len(names)):
    val += (i + 1) * sum(ord(c) - start for c in names[i].strip('"'))

  return val
