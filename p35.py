import time
import math

def timeit(n):
  start = time.time()
  print(primes(n))
  print(time.time() - start)


def isprime(n):
  sqrt = int(math.sqrt(n)) + 1
  return all(n % i for i in range(2, sqrt))

def primes(n):
  results = 2
  for i in range(7, n, 2):
    s = str(i)
    digits = len(s)

    if '0' in s:
      continue

    if '2' in s:
      continue

    if '4' in s:
      continue

    if '5' in s:
      continue

    if '6' in s:
      continue

    if '8' in s:
      continue

    for j in range(digits):
      if not isprime(i):
        break
      i = (i % 10) * (10 ** (digits - 1)) + int(i / 10)
    else:
      results += 1
  return results




