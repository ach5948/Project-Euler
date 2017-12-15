import math

def sieve(n):
  a = set(range(3, n + 1, 2))
  a.add(2)
  for i in range(3, int(n/2) + 1, 2):
    if i in a:
      a.difference_update(range(2 * i, n, i))
      
  return a

def factor(n):
  sqrt = int(math.sqrt(n)) + 1
  primes = sieve(sqrt)

  for i in range(sqrt, 0, -1):
    if not n % i:
      if i in primes:
        return i


