def ones(x):
  if x is 0:
    return ""

  elif x is 1:
    return "one"
  
  elif x is 2:
    return "two"

  elif x is 3:
    return "three"

  elif x is 4:
    return "four"
  
  elif x is 5:
    return "five"

  elif x is 6:
    return "six"

  elif x is 7:
    return "seven"

  elif x is 8:
    return "eight"

  elif x is 9:
    return "nine"

  else:
    return ""


def prefix(x):
  if x is 3:
    return "thir"

  elif x is 5:
    return "fif"

  elif x is 8:
    return "eigh"

  else:
    return ones(x)

def teens(x):
  if x is 0:
    return "ten"

  elif x is 1:
    return "eleven"

  elif x is 2:
    return "twelve"

  else:
    return prefix(x) + "teen" 

def tens(number):
  x = int(number / 10) 
  y = number % 10
  if x is 0:
    return ones(y)

  if x is 1:
    return teens(y)

  elif x is 2:
    result =  "twenty"

  elif x is 4:
    result = "forty"

  else:
    # prefix + ty + ones
    result = prefix(x) + "ty"

  if y:
    result += "-" + ones(y)
  return result

def hundreds(number):
  x = int(number / 100)
  y = number % 100

  result = ""

  if x:
    # ones + "hundred"
    result += ones(x) + " hundred"
    if y:
      result += " "

  if y:
    result += tens(y)

  return result

def thousands(number):
  x = int(number / 1000)
  y = number % 1000

  result = ""

  if x:
    result += hundreds(x) + " thousand"
    if y:
      result += " "

  if y:
    result += hundreds(y)

  return result

def millions(number):
  x = int(number / 1000000)
  y = number % 1000000

  result = ""

  if x:
    result += hundreds(x) + " million"
    if y:
      result += " "

  if y:
    result += thousands(y)

  return result
