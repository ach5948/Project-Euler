import time
import math

def isprime(n):
  if n < 2:
    return False
  sqrt = int(math.sqrt(n)) + 1
  return all(n % i for i in range(2, sqrt))

def sieve(n):
  a = set(range(3, n + 1, 2))
  a.add(2)
  for i in range(3, int(n/2) + 1, 2):
    if i in a:
      a.difference_update(range(2 * i, n, i))
  return a

def main():
  results = []
  num = 11
  while len(results) < 11:
    check = str(num)
    skip = [0, 4, 6, 8]
    if any(str(j) in check for j in skip):
      num += 2
      continue
    if isprime(num):
      s = str(num)
      for j in range(len(s)):
        # check left to right
        if not isprime(int(s[j:])):
          break
        if not isprime(int(s[:len(s) - j])):
          break
      else:
        results.append(num)
    num += 2


  total = sum(results)
  return results, total

