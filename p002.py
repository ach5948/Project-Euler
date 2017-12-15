
def main(n):
  a = 1
  b = 2
  total = 0
  while b < n:
    if not b % 2:
      total += b

    c = a
    a = b
    b = a + c

  return total


