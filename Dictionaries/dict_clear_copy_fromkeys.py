
# CLEAR, COPY, FROMKEYS
# a = {"a":10, "b":20, "c":30}
# print(a)
#
# # CLEAR:
# # removes all the data in the dictionary on which it is called
# a.clear()
# print(a)
#
# # COPY:
# # returns a copy of a particular dictionary
# b = a.copy()
#
# print(b)

# FROMKEYS:
# creates a dictionary from a list/tuple/set
# the values taken from list/tuple/set become keys of the dictionary
# if no value is given, then each key defaults to NONE
# if a value is provided, then each key will have the defined value
# repeated values will be omitted
seq = ('name', 'age', 'name')
out = dict.fromkeys(seq, 23)
print(out)