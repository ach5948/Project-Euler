def isPandigital(x, n):
  check = str(x)
  for i in range(1, n + 1):
    if check.count(str(i)) != 1:
      return False
  return True
  
def main():
  products = set()
  digits = [i for i in range(1, 10)]

  # 1 by 4
  for i in range(len(digits)):


  
