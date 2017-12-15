def palindrome(x):
  for i in range(len(x)):
    if x[i] != x[-(i + 1)]:
      return False
  return True

def check(x):
  if not palindrome(str(x)):
    return False

  if not palindrome(bin(x)[2:]):
    return False

  return True

def main(n):
  return sum(i * check(i) for i in range(1, n))

