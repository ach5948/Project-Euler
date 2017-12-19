def readin(filename):
  m = []
  with open(filename, 'r') as fopen:
    m = [[int(j) for j in i.strip('\n').split(' ')] for i in fopen]
  return m

def check_neighbors(n, m, r, c):
  s = []
  result = 0
  for i in range(2):
    for j in range(-1, 2):
      # ignore center
      if not i and not j:
        continue

      # too small
      if r + i * n < 0:
        continue
      if c + j * n < 0:
        continue

      # too big
      if r + i * n > len(m):
        continue
      if c + j * n > len(m[0]):
        continue

      value = 1
      for k in range(n):
        value = value * m[r + i * k][c + j * k]
      if value > result:
        result = value

  return result

def check(n):
  m = readin("p011.txt")

  most = 0

  for i in range(len(m)):
    for j in range(len(m[0])):
      temp = check_neighbors(n, m, i, j)

      if temp > most:
        most = temp

  return most






