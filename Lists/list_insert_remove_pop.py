# THis file consists of insert, remove and pop operations

a = [10, 20, 30, 40, 50]
print("original list")
print(a)

# Insert:
# inserts a value before the index specified
# here '2' is the index before which the value has to be inserted and 33 is the value to be inserted
a.insert(2, 33)
print("list after inserting a value 33 before the index 2")
print(a)

# b = a
#
# b.insert(3, 32)
# print(a)

# Remove:
# specify the value to be removed (NOT THE INDEX)
# if the value is not present, it gives out a ValueError

a.remove(10)
print("list after removing VALUE:10")
print(a)

# a.remove(3) # gives an error since it is not present in the list

# POP:
# removes the element specified by it's index position
# INDEX has to be specified and NOT THE VALUE
a.pop(2)
print("value after popping the value at index 2")
print(a)


# if index is not specified - the last item in the list is removed
a.pop()
print("value after popping the last value")
print(a)

# a.pop(7) -> gives and IndexError






