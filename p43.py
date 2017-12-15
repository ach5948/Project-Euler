import itertools

def find():
  total = 0
  for i in itertools.permutations("0123456789"):
    if int(i[1] + i[2] + i[3]) % 2:
      continue

    if int(i[2] + i[3] + i[4]) % 3:
      continue

    if int(i[3] + i[4] + i[5]) % 5:
      continue

    if int(i[4] + i[5] + i[6]) % 7:
      continue

    if int(i[5] + i[6] + i[7]) % 11:
      continue

    if int(i[6] + i[7] + i[8]) % 13:
      continue

    if int(i[7] + i[8] + i[9]) % 17:
      continue

    total += int("".join(i))

  return total
