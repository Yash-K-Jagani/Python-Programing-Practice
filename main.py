n = int(input())

for row in range(1, n + 1):
  for col in range(1, n + 1):
    print((row * col) % 10, end="")
  print()
