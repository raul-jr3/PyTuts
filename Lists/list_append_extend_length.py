# this file consists of list operations : append, extend, length

# create a list
a = [10, 20, 30, 40, 50]
print("original list")
print(a)

#Append:
# to add an element at the end of the list: use the append method
print("appending 35 to 'a'")
a.append(35)
print(a)

# Extend :
# suppose we have a list b, now we append this b to a
b = [10, 20]

# when we do this, the list itself gets added to the list 'a'
# a.append(b)

# print(a)

# but, if we want to add only the values of the list b to a, then we use extend
a.extend(b)
print(a)

# to find out the number of items present inside a list or to find out it's length
# use the length method
print("printing out the length of 'a'")
print(len(a))

# if we have appended or added a list inside a list
c = [20, 30]
a.append(c)
print(a)

# now if we print a[9]
print(a[8]) # we get both values that are present in the list
# in order to get each value inside the list

print(a[8][0])
# print(a[6][0])






