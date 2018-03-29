
# LIST COMPREHENSIONS

a = [1, 2, 4, 5, 65, 44, 3, 4]

# List comprehensions provide a concise way to create lists
result = [x for x in a if x % 2 == 0]
print(result)


squares = [x**2 for x in a]

# The above function will be equivalent to:
# def squares(list_of_numbers):
#     square = []
#     for i in list_of_numbers:
#         square.append(i**2)
#     return square
# print(squares(a))

print(squares)