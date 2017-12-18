import math

def sieve(n):
  a = set(range(3, n + 1, 2))
  a.add(2)
  for i in range(3, int(n/2) + 1, 2):
    if i in a:
      a.difference_update(range(2 * i, n, i))
  return a

def main(a_max, b_max):
  prime = sieve(a_max * b_max)
  max_n = 0
  max_a = 0
  max_b = 0
  for a in range(1 - a_max, a_max):
    for b in range(-b_max, b_max + 1):
      n = 0
      while True:
        check = n**2 + a * n + b
        if check not in prime:
          break
        if n > max_n:
          max_n = n
          max_a = a
          max_b = b
        n += 1

  return max_a * max_b, max_a, max_b, max_n

