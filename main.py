text = input()

# TODO: build a new string whose first and last characters are swapped,
# with every character between them left where it is.
# Remember that a very short string has nothing to swap.
if len(text) > 1:
  result = text[-1] + text[1:-1] + text[0] 
else:
  result = text

print(result)
