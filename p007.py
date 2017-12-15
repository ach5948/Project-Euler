def isprime(x):
  sqrt = int(x ** 0.5) + 1
  return all(x % i for i in range(2, sqrt))

def main(n):
  pnum = 1
  check = 2
  while pnum < n:
    check += 1
    if isprime(check):
      pnum += 1

  return check
