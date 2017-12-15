def find(n):
  top = 10 ** n - 1
  bottom = 10 ** (n - 1) - 1
  results = []
  t, p = findfirst(top, bottom)
  for i in range(top, min(t,p) - 1, -1):
    for j in range(top, min(t,p) - 1, -1):
      s = str(i * j)
      l = int(len(s) / 2)
      for let in range(l):
        if s[let] != s[-(let + 1)]:
          break
      else:
        results.append(i * j)
  return max(results)
  
def findfirst(top, bottom):
  for i in range(top, bottom, -1):
    for j in range(top, bottom, -1):
      s = str(i * j)
      l = int(len(s) / 2)
      for let in range(l):
        if s[let] != s[-(let + 1)]:
          break
      else:
        return i, j
