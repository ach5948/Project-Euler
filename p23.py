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

def findall():
  nums = set() 

  nums = set(i for i in range(1, 28124) if sum_divs(i) > i)

  result = 0
  for i in range(28124):
    if not any(i - j in nums for j in nums):
      result += i
  
  return result

