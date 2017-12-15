def test(n):
  number = 1

  while True:
    value = sorted(str(number))
    for i in range(2, n + 1):
      s = str(number * i)
      s = sorted(s)
      if s != value:
        break
    else:
      break

    number += 1

  return number

