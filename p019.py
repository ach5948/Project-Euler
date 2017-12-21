def isleap(x):
  if x % 4:
    return False
  if not x % 400:
    return True
  if not x % 100:
    return False
  
  return True

def monthDays(x, y):
  days = 0
  x = x % 12
  if x == 1:
    if isleap(y):
      days = 29
    else:
      days = 28
  else:
    if (x % 7) & 1:
      days = 30
    else:
      days = 31

  return days

def yearDays(x):
  days = 0
  if isleap(x):
    days = 366
  else:
    days = 365

  return days

def addMonth(s):
    s[0] += 1
    if s[0] >= 12:
      s[2] += 1
      s[0] = s[0] % 12
    s[1] = 1


# start: (month, day, year)
#   end: (month, day, year)
def countDays(day, start, end):
  s = list(start)
  e = list(end)

  # switch from 1-12 to 0-11
  s[0] -= 1
  e[0] -= 1

  if s[1] != 1: 
    addMonth(s)
  
  disp = 1
  for i in range(1900, s[2]):
    disp += yearDays(i)
    disp = disp % 7
  print(disp)

  for i in range(1, s[0]):
    disp += monthDays(i, s[2])
    disp = disp % 7

  days = 0
  while True:
    if s[2] > e[2]:
      break
    if s[2] == e[2]:
      if s[0] > e[0]:
        break
      if s[0] == e[0]:
        if s[1] > e[1]:
          break
    
    if disp == day:
      days += 1

    disp += monthDays(s[0], s[2])
    disp = disp % 7
    addMonth(s)
    
  return days



