def count(p):
  sols = []
  for a in range(1, p - 1):
    b = p / 2 * (p - 2 * a) / (p - a)
    c = p - a - b

    if int(b) != b:
      continue
    if b <= 0:
      continue
    if c <= 0:
      continue
    
    if not any(a in i for i in sols):
      sols.append((a, b, c))
  return len(sols), sols

def right(n):
  max_sol = 0
  max_p = 0
  for p in range(1, n + 1):
    num, c = count(p)
    if num > max_sol:
      max_sol = num
      max_p = p

  return max_p



