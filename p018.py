def readin(filename):
  tree = []
  with open(filename, "r") as fopen:
    for line in fopen:
      a = line.split(' ')
      tree.insert(0, [int(i) for i in a])
  return tree

def find(filename):
  a = readin(filename)
  for i in range(1, len(a)):
    for j in range(len(a[i])):
      a[i][j] += max(a[i - 1][j], a[i - 1][j + 1])

  return a[-1][0]

def p018():
  return find("p018.txt")

def p067():
  return find("p067.txt")
