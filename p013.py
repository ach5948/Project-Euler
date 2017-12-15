def main(n):
  total = 0
  with open("p013.txt", "r") as fopen:
    for i in fopen:
      total += int(i.strip("\n"))

  return str(total)[0:n]


