def main(n):
  easy = int((n + 1) * n / 2)
  easy = easy * easy

  hard = sum(i * i for i in range(1, n + 1))
  return easy - hard
