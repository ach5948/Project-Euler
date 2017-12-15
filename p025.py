def main(n):
  a = 0
  b = 1
  index = 1
  while len(str(b)) < n:
    c = a
    a = b
    b = a + c

    index += 1

  return index


