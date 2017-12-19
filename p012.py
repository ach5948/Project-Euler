import time
import math

def factors(x):
  sqrt = math.sqrt(x)
  top = int(sqrt) + 1
  val = 2 * sum(not (x % i) for i in range(1, top))
  
  if int(sqrt) == sqrt:
    val -= 1
  
  return val

def square(n):
  start = time.time()
  number = 1
  add = 2
  while(True):
    if factors(number) > n:
      break

    number += add
    add += 1

  print(time.time() - start)
  return number


def fast(n):
  start = time.time()
  cnt = 0
  i = 1
  while True:
    if i % 2:
      cnt = factors(i) * factors((i + 1) / 2)
    else:
      cnt = factors(i / 2) * factors(i + 1)
    if cnt > n:
      break
    i += 1
    
  print(time.time() - start)
  return int(i * (i + 1) / 2), cnt
