import time

def isPandigital(n):
  check = str(n)
  for i in range(1, 10):
    if check.count(str(i)) != 1:
      return False
  return True
  
def main():
  start = time.time()
  products = set()

  for i in range(1, 9):
    for j in range(1234, 9876):
      check = i * j
      if check > 9876:
        break
      if isPandigital(str(i) + str(j) + str(i * j)):
        products.add(i * j)

  for i in range(12, 98):
    for j in range(123, 987):
      check = i * j
      if check > 9876:
        break
      if isPandigital(str(i) + str(j) + str(i * j)):
        products.add(i * j)
  
  result = sum(products)

  print(time.time() - start)

  return result


  
