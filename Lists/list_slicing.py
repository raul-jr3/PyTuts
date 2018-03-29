# # This file consists of copying a list, printing out a particular value,
# # manipulating a particular value, printing out each value in a list
#
# # create a list
a = [10, 20, 30, 40, 50]
print("original list")
print(a)

# to get a particular value in a list, we use the index of that value
# to get the third value:
print("printing a particular value")
print("value of the third element in the list 'a' : %d" % a[2])

# lists are mutable, meaning the values inside a list can be changed:
# suppose if we want to change the second value inside a list, we do it like so:
a[1] = 35
print("after the value has changed:")
print(a)

# this makes a reference to 'a', so whatever the changes you do in b is reflected in a
print("copied list 'b' from 'a'(copied as a reference to 'a')")
b = a
print(b)

# change the second value in b
b[1] = 45

# the change is reflected in 'a' also
print("manipulated 'b'")
print(b)
print("the changes done in 'b' is also reflected in 'a'")
print(a)

a[3] = 70

print("manipulated 'a'")
print(a)
print("likewise, the changes made in 'a' is reflected in b")
print(b)
# print(a)

# this creates a copy of list 'a'
print("copied list 'c' from 'a'(list 'c' is created as a copy of 'a')")
c = a[:]

# any changes made to list c is not reflected in 'a'
c[2] = 1
print("list c")
print(c)

# likewise any changes made in a are not reflected in c
a[4] = 2
print("list a")
print(a)


# to print values in a particular range:
print("values from index 2 to 4")
print(a[2:5])

# To get all the values:
# print(a[:])

# to get all the value from first to a particular index:
# print(a[:3]

# to reverse a list:
# print("reverse of the list:")
# print(a[::-1])

# to print each value, iterate over each value and print...use a for loop
for i in a:
    print(i)