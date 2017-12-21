import time

def sieve(n):
  a = set(range(3, n + 1, 2))
  a.add(2)
  for i in range(3, int(n/2) + 1, 2):
    if i in a:
      a.difference_update(range(2 * i, n, i))
  return a

def main(n):
  start = time.time()
  primes = sieve(n)
  lst = sorted(primes)
  top = 0
  prime = 0

  print(time.time() - start)

  # starting with 2
  check = 0
  for i in range(1, len(lst), 2):
    check += lst[i - 1]
    check += lst[i]
    if check in primes:
      if (i + 1) > top:
        top = (i + 1)
        prime = check

    if check > n:
      break

  for i in range(1, len(lst)):
    check = lst[i]
    for j in range(i + 1, len(lst) - 1, 2):
      check += lst[j]
      check += lst[j + 1]
      
      if check in primes:
        if (j + 2) - i > top:
          top = (j + 2) - i
          prime = check
      
      if check > n:
        break

  print(time.time() - start)

  return prime, top


