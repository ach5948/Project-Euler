import time

def permute(lst, value):
  if len(lst) == 1:
    if not (value % lst[0]):
      return 1
    else:
      return 0

  result = 0
  top = int(value / lst[0])
  for i in range(top + 1):
    result += permute(lst[1:], value - (lst[0] * i))
  
  return result

def main(n):
  start = time.time()
  result = permute([200, 100, 50, 20, 10, 5, 2, 1], n)
  print(time.time() - start)

  return result

