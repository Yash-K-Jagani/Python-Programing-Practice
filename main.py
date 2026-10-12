# Line 1 of the input is a whole number, line 2 is a decimal number.
whole_text = input()
decimal_text = input()

# TODO: turn the two lines of text into numbers and add them up
whole_int = int(whole_text)
decimal_float = float(decimal_text)

total_1 = whole_int + decimal_float
total_2 = int(total_1)

print(total_1)
print(total_2)
print(f"{whole_int} + {decimal_float} = {total_1}")