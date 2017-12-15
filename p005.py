import sys

def smult(n):
  factors = []
  for i in range(1, n + 1):
    num = i
    for j in factors:
      if not i % j:
        num = int(num / j)
    if num not in [0, 1]:
      factors.append(num)

  result = 1
  for i in factors:
    result *= i
  return result

if __name__ == "__main__":
  print(smult(int(sys.argv[1])))
  sys.exit()
