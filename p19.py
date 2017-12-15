def isleap(x):
  if x % 4:
    return False
  if not x % 400:
    return True
  if not x % 100:
    return False
  
  return True

def monthDays(x, y):
  x = (x - 1) % 12
  if x == 1:
    if isleap(y):
      return 29
    else:
      return 28
  if (x % 7) & 1:
    return 30
  else:
    return 31

def yearDays(x):
  if isleap(x):
    return 366
  else:
    return 365

def addMonth(s):
    s[0] += 1
    if s[0] > 12:
      s[2] += 1
      s[0] = s[0] % 12
    s[1] = 1


# start: (month, day, year)
#   end: (month, day, year)
def countDays(day, start, end):
  s = list(start)
  e = list(end)
  if s[1] != 1: 
    addMonth(s)
  
  disp = 1
  for i in range(1900, s[2]):
    disp += yearDays(i)
    disp = disp % 7

  for i in range(1, s[0] + 1):
    disp += monthDays(i, s[2])

  while s[0] <= e[0] and s[1] <= e[1] and s[2] <= e[2]
    



