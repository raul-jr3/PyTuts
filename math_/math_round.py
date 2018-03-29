

# ROUND
# The round function, as the name suggests, rounds off a
# floating point number with the digits specified

# suppose if I declare a variable which holds a value of 23.323834
a = 23.323834

# now I call round on that variable, to round it's value by 2 digits after the decimal point
result = round(a, 2)

# the round function is really intelligent
# suppose I have a variable which holds a value fo 23.0005
b = 23.0005

# now I call round on this value with 2 digits
output = round(b, 2)

# now, instead of printing 23.00, it just prints 23.0 *_*
print(output)

# print(result)