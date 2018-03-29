
# FORMAT:
# the format function can be used to add values inside a statement

# Suppose we have a string "Way"
a = "way"

# and we want to add this in the print statement

# the '{}' is used as a placeholder
print("Where there is a will, there is a {}".format(a))

# It can be at any place inside a string
b = "road"

print("where there is a {}, there is a way!".format(b))

# it can also have multiple placeholders
print("where ther is a {}, there is a {}".format(b, a))

# to unpack a string, use the '*' in front of the string_value
# NOTE: the number of placeholders has to equal to the number of characters present in the
# string to be unpacked
print("blah {}{}{}{}".format(*'swag')) # this is similar to *args

# we can also specify the order in which the characters appear in the output
# by specifying the index values inside the placeholder
print("blah {3}{0}{1}{2}".format(*'swag'))

# to specify the spaces between each character,
# we can specify the number of spaces inside the placeholder after the ':'
print("blah {:3}{:3}{:3}{:3}".format(*'swag'))

# we can also specify the direction in which the spaces has to printed
print("blah {:<3}|{:^4}|{:>3}|{:<3}".format(*'swag'))


# we can also use the dictionary values
# this needs to have placeholders which are equal to the number of keys in the dictionary
values = dict(a=10, b=20, c=30)
print("blah :{a} {b} {c}".format(**values)) # similar to **kwargs

# if there are not enough placeholders to hold all the values in the dictionary,
# then the remaining values will be omitted


a = [10, -20, 30]
print("blah : {1:>3} | {0:^5}|".format(a[0], a[1]))

# we can also get the value of a number in decimal, binary, hex and octal format
print("blah : {:b} {:x} {:o} {:d}".format(a[0], a[0], a[0], a[0]))

print("positive value: {}, negative value: {:+}".format(a[0], a[1]))

# we can use ',' to separate values in terms of thousands
print("rich kid: {:,}".format(1234567890))