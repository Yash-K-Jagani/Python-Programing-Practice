code = input()
amount = int(input())

# Replace each placeholder below with the comparison described in the comment.
print("GOLD" == code)  # TODO: is the code exactly GOLD?
print("X" in code)  # TODO: does the code contain an X?
print(amount > 49 and amount < 201)  # TODO: is the amount between 50 and 200, both ends included?
print("GOLD" == code or amount > 200 or amount < 50)  # TODO: exactly GOLD, or the amount outside that band?