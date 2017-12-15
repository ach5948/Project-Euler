def hand(n):
  # < 1000
  n = n - 1

  # 3's
  a = int(n / 3)
  b = int(3 * a * (a + 1) / 2)

  # 5's
  a = int(n / 5)
  b += int(5 * a * (a + 1) / 2)

  # duplicates
  a = int(n / (3 * 5))
  b -= int((3 * 5) * a * (a + 1) / 2)

  return b

def main(n):
  a = [3, 5]
  nums = set()
  for i in a:
    nums.update(set(range(i, n, i)))
  return sum(nums)
