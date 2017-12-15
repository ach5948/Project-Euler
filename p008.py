def product(x):
  value = 1
  for c in x:
    value = value * int(c)
  return value

def main(n):
  with open("p008.txt", 'r') as fopen:
    a = fopen.readline().strip('\n')

  s = list(filter(lambda x: len(x) >= n, a.split('0')))

  most = 0
  for i in s:
    start = 0
    stop = n
    while stop <= len(i):
      temp = product(i[start: stop])
      if temp > most:
        most = temp
      start += 1
      stop += 1

  return most



