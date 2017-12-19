import time

def sieve(n):
  a = set(range(3, n + 1, 2))
  a.add(2)
  for i in range(3, int(n/2) + 1, 2):
    if i in a:
      a.difference_update(range(2 * i, n, i))
  return a


def period(n):
  r = set()
  num = 1
  
  while True:
    test = 10**num % n
    if test in r:
      break
    r.add(test)
    num += 1

  return num


def main(n):
  start = time.time()
  primes = sieve(n)
  top = 0
  value = 0
  for i in primes:
    check = period(i)
    if check > top:
      top = check
      value = i

  print(time.time() - start)

  return value, top


def slow(n):
  start = time.time()
  top = 0
  value = 0
  for i in range(2, n):
    check = period(i)
    if check > top:
      top = check
      value = i

  print(time.time() - start)

  return value, top
