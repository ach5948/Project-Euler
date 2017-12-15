import time

def sieve(n):
  start = time.time()
  a = set(range(3, n + 1, 2))
  a.add(2)
  for i in range(3, int(n/2) + 1, 2):
    if i in a:
      a.difference_update(range(2 * i, n, i))
      
  print(time.time() - start)
  return a


