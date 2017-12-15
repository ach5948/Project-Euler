def check(n):
  results = []
  digits = 2
  while (10 ** digits) - 1 <= (9 ** n) * digits:
    digits += 1

  top = (10 ** digits) - 1

  for i in range(10, top):
    val = sum(int(j) ** n for j in str(i))
    if val == i:
      results.append(i)

  return sum(results), results

