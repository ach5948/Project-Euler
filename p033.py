import time

def main():
  start = time.time()
  results = []

  for i in range(11, 100):
    for j in range(10, i):
      for k in str(i):
        if k == '0':
          continue

        if k not in str(j):
          continue

        a = int(str(i).replace(k, '', 1))
        b = int(str(j).replace(k, '', 1))

        if not a or not b:
          continue

        if (i / j) == (a / b):
          results.append((j, i))

  num = 1
  dem = 1
  for i in results:
    num *= i[0]
    dem *= i[1]

  print(time.time() - start)

  return results, num, dem
