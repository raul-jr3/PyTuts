import json

# to declare a json:
# similar to a dictionary, but enclosed within quotes
# if the quotes are missed it is considered as a dictionary and the json ops won't work on it
data = '{"three":"sala", "bandhu":"hogu"}'

# the json.loads(s for string) function
input_data = json.loads(data)

# if we try to print this it will give out the values in unicode format
print(input_data)

# in order to get it in the format in which the data was present
# we use the json.dumps function
output_data = json.dumps(input_data)

# now, we get the output in the format in which it was read
# print(output_data)