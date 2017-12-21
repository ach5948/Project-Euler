import time

def sieve(n):
  a = set(range(3, n + 1, 2))
  a.add(2)
  for i in range(3, int(n/2) + 1, 2):
    if i in a:
      a.difference_update(range(2 * i, n, i))
  return a

def signature(n):
  values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
  sig = 1
  for c in str(n):
    sig *= values[int(c)]
  return sig

def main(n):
  start = time.time()
  primes = sieve(10**(n))
  primes.difference_update(range(10**(n - 1)))
  perms = dict()
  
  for i in primes:
    entry = signature(i)
    if entry in perms:
      perms[entry].append(i)
    else:
      perms[entry] = [i]

  values = []
  for i in perms.values():
    if len(i) > 2:
      values.append(sorted(i))

  finals = set()
  for i in values:
    for j in i:
      for k in i:
        if j == k:
          continue
        
        diff = k - j
        if j + 2 * diff in i:
          finals.add(tuple(sorted([j, k, j + 2 * diff])))

  finals = sorted(finals)
  print(time.time() - start)
  
  return finals
