

# similar to lists, dictionary comprehensions provides a concise way to build dictionaries
a = [1,2,3,5,3,2,4]

result = {x: x**2 for x in a}
print(result)