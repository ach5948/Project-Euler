import math

def sum_divs(i):
  sqrt = int(math.sqrt(i)) 
  val = 1
  for j in range(2, sqrt + 1):
    if not (i % j):
      val += j

      if i / j != j:
        val += i / j
  return val

def sum_all(n):
  result = 0
  for i in range(1, n):
    a = sum_divs(i)
    b = sum_divs(a)
    if b == i and b != a:
      result += i

  return result


