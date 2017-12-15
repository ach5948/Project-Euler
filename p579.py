def cube_sum(x):
  return (x + 1) ** 3

def all_sum(n):
  total = 0
  for i in range(1, n + 1):
    total += cube_sum(i) * cube_sum(n - i)
  return total
