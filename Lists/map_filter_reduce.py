# FILTER, MAP, REDUCE

# let's say we have a function which checks if the number is even or not
def check_even(number):
    return number % 2 == 0

a = [10, 2, 3, 5, 6, 3]

# FILTER:
# The filter function takes in a function and a sequence of numbers and
# returns the value which are true for the function
# filter function returns a list
print(filter(check_even, a))

# MAP:
# map takes in a function and a sequence of numbers and maps each value
# from the numbers with the function and returns a list

def square(x):
    return x * x

print(map(square, a))
