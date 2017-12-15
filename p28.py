def diagonals(n):
  layers = int((n + 1) / 2)

  total = 1
  value = 1
  for i in range(1, layers):
    for j in range(4):
      value += 2 * i
      total += value

  return total
