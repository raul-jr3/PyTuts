
# cmp, len, type

# CMP:
#
a = dict(apple=35, mango=45, papaya=55)
# the dictionary compare function returns
# a value of -1 if they are not equal,
# a value of 0 if they are equal,
# a value of 1 if dict1 < dict2
b = dict(apple=35, mango=45, papaya=55)


# if dict1 and dict2 have same number of values, it returns 1
# the cmp function returns 0 only if the number of values and the values are same in both
# the dictionaries
c = dict(a=10, b=20, c=30)

print(cmp(a, c))

# LEN:
# returns the length of a dictionary
print(len(a))

# TYPE:
# returns the type of data passed
print(type(a))









