
import base64

a = 'blah blah blah'
# encode the string value
encoded_data = base64.encodestring(a)

# take a look
# print(encoded_data)

# on the receiving end
# decode the data
decoded_data = base64.decodestring(encoded_data)

# if we look at the decoded_data
print(decoded_data)

# we have our string :)