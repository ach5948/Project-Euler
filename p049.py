import time

def sieve(n):
  a = set(range(3, n + 1, 2))
  a.add(2)
  for i in range(3, int(n/2) + 1, 2):
    if i in a:
      a.difference_update(range(2 * i, n, i))
  return a

def digit_sort(n):
  a = [int((n % 10**(i + 1)) / 10**i) for i in range(len(str(n)))]
  a.sort(reverse=True)
  return sum(a[i] * 10**i for i in range(len(a)))

def sort_purge(x):
  if len(x) < 3:
    return False
  x.sort()
  return True

def main(n):
  start = time.time()
  primes = sieve(10**(n))
  primes.difference_update(range(10**(n - 1)))

  finals = []

  for i in range(2, int(.45 * 10**n), 2):
    for j in primes:
      check = digit_sort(j)
      t1 = j + i

      if t1 not in primes:
        continue
      if check != digit_sort(t1):
        continue

      t2 = j + 2 * i

      if t2 not in primes:
        continue

      if check != digit_sort(t2):
        continue
      
      finals.append((j, t1, t2))

  print(time.time() - start)
  
  return finals
