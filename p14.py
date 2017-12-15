def seq(x):
  val = x
  chain = 0
  while val != 1:
    if val % 2:
      val = 3 * val + 1
    else:
      val = val / 2
    chain += 1

  return chain

def longest(n):
  top = 0
  val = 0

  for i in range(1, n):
    temp = seq(i)
    if temp > top:
      top = temp
      val = i

  return val, top
