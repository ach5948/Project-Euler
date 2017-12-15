import math

def factors(x):
  sqrt = math.sqrt(x)
  top = int(sqrt) + 1
  val = 2 * sum(not (x % i) for i in range(1, top))
  
  if int(sqrt) == sqrt:
    val -= 1
  
  return val

def square(n):
  number = 1
  add = 2
  while(True):
    if factors(number) > n:
      break

    number += add
    add += 1

  return number
