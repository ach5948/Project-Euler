import math

def check(x):
  return sum(math.factorial(int(i)) for i in str(x)) == x

def main():
  return sum(i * check(i) for i in range(3, 10 ** 7))


