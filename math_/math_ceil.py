
import math

# CEIL
# this returns the smallest integer which is greater than or equal to the
# number on which the ceil is applied

# suppose I have a variable a which holds a value 23.03
a = 23.66

# I call ceil on that variable
result = math.ceil(a)

print(result)

b = -23.99

# now if I call ceil on this negative number...
output = math.ceil(b)

# the output is the previous number of it even if the value after the decimal point
# is greater than 0.5
print(output)

# Conclusion:
# if ceil is applied on a positive number,
# the number next to it is returned(irrespective of the value after the decimal point)(ex: 23.03 -> 24.0)
# and if ceil is applied on a negative number,
# the number previous to it is returned(irrespective of the value after the decimal point) (ex: -23.93 -> -23.0)
