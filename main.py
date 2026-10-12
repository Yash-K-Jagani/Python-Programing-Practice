score = int(input())

# TODO: work out which band `score` falls in and print its single letter.
# Print exactly one of: A B C D F
if score > 90 or score == 90:
  print("A")
elif score > 79 and score < 90:
  print("B")
elif score > 69 and score < 80:
  print("C")
elif score > 59 and score < 70:
  print("D")
else:
  print("F")