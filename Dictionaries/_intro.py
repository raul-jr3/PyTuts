
# a dictionary can be created as follows:

# using the constructor
a = dict()

# or like:
# a = {}


# to add a new value into the dictionary:
a["physics"] = 78
a["maths"] = 68
a["chemistry"] = 55

print(a)
#
# # the keys() function returns all the keys in a dictionary
print(a.keys())

# # the values() function returns all the values in a dictionary
print(a.values())

# to access a particular value use it's key
print(a["physics"])

# to delete a particular value:
del a["physics"]
print(a)

# dictionaries are mutable meaning their values can be changed
a["physics"] = 77
print(a)

# The dict constructor can build dictionaries from sequences of key-value pairs
c = dict([('apple', 35), ('mango', 45), ('pineapple', 55)])
print(c)

d = dict(red=3, blue=2, green=1)
print(d)










