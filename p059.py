import itertools

def attack1(filename, pass_len):
  with open(filename) as fopen:
    msg = fopen.readline().strip('\n')
    msg = msg.split(',')

  array = [[int(msg[i]) for i in range(len(msg)) if i % pass_len == j] for j in range(pass_len)]

  for i in range(ord('a'), ord('z') + 1):
    for j in range(ord('a'), ord('z') + 1):
      for k in range(ord('a'), ord('z') + 1):
        msg = ""
        for x in range(len(array[0])):
          msg += chr(array[0][x] ^ i)
          if x < len(array[1]):
            msg += chr(array[1][x] ^ j)
          if x < len(array[2]):
            msg += chr(array[2][x] ^ k)

        if " a " not in msg:
          continue

        if " is " not in msg:
          continue
        
        return msg
         

def attack2(filename, pass_len):

  with open(filename) as fopen:
    msg = fopen.readline().strip('\n')
    msg = msg.split(',')

  freq = {}
  for i in range(ord('a'), ord('z') + 1):
    freq[i] = 0
    for j in range(len(msg)):
      if int(msg[j]) ^ i == ord(' '):
        freq[i] += 1

  vals = sorted(freq, key = lambda x: freq[x], reverse=True)

  keys = [vals[i] for i in range(pass_len)]

  for i in itertools.permutations(keys):
    s = ""
    for j in range(len(msg)):
      s += chr(int(msg[j]) ^ i[j % len(i)])

    if " is " not in s:
      continue

    if " the " not in s:
      continue

    return s
