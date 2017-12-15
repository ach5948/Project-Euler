import math

def rdiv(x, y):
  result = int(x / y)
  remainder = x % y

  # Round off error correction
  if (result * y) + remainder > x:
    result -= 1

  return result, remainder


def permute(array, index):
  nums = list(array)

  if index >= math.factorial(len(nums)):
    print("Index value too big for number of digits")
    return

  value = index
  ans = ""
  for i in range(len(nums) - 1, 0, -1):
    fact = math.factorial(i)
    temp, value = rdiv(value, fact)
    ans += str(nums.pop(temp))

  ans += str(nums.pop())
  return ans

