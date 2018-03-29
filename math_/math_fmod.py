
import math
# FMOD:
# it returns the mod value(the remainder)

# suppose we have two numbers a and b
a = 11
b = 3

# when I call fmod on a and b
result = math.fmod(a, b)

# we get the remainder in float
print(result)

# instead of importing math and calling fmod,
# we can just do:
result2 = a % b

# but doing this(a % b) gives out the result in integer
print(result2)
