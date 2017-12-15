def prefix(x):
  if x is 1:
    # one
    return 3
  
  if x is 2:
    # two
    return 3

  if x is 3:
    # thir
    return 4

  if x is 4:
    # four
    return 4
  
  if x is 5:
    # fif
    return 3

  elif x is 6:
    # six
    return 3

  elif x is 7:
    # seven
    return 5

  elif x is 8:
    # eigh
    return 4

  elif x is 9:
    # nine
    return 4

  else:
    return 0


def ones(x):
  if x is 0:
    return 0

  elif x is 3:
    # three
    return 5

  elif x is 5:
    # five
    return 4

  elif x is 8:
    # eight
    return 5

  else:
    return prefix(x)

def teens(x):
  if x is 0:
    # ten
    return 3

  elif x is 1:
    # eleven
    return 6

  elif x is 2:
    # twelve
    return 6

  else:
    return prefix(x) + 4 

def tens(number):
  x = int(number / 10) 
  y = number % 10
  if x is 0:
    return 0 + ones(y)

  if x is 1:
    return teens(y)

  elif x is 2:
    # twenty
    return 6 + ones(y)

  elif x is 4:
    # forty
    return 5 + ones(y)

  else:
    # prefix + ty + ones
    return prefix(x) + 2 + ones(y)

def hundreds(number):
  x = int(number / 100)
  y = number % 100

  val = 0
  if x:
    # ones + "hundred"
    val += ones(x) + 7
    if y:
      # and
      val += 3

  if y:
    val += tens(y)

  return val

def main():
  result = sum(hundreds(x) for x in range(1, 1000))
  # one thousand
  result += 11
  return result

