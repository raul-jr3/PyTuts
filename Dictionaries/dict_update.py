
# UPDATE:
# similar to extend for lists

a = dict(a=23, b=33, c=12)

b = dict(d=23)

# this extends the b dictionary with the values of a
# the update happens in alphabetical order
b.update(a)
# a.update(b)

# print(a)

print(b)
