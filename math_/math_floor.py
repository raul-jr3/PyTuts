

import math
# FLOOR
# the floor function returns the largest integer which is less than or equal to the
# number on which floor is applied

a = 23.66

# so when the floor is applied on 23.66 the greatest value which is <= 23.66 is 23.0
result = math.floor(a)


# so this returns 23.0
print(result)

# and if we have a negative value
b = -23.77

# then I apply floor on it
output = math.floor(b)

# the output will be -24.00 because -24.00 < -23.77
print(output)
