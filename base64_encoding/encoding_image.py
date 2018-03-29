
# ENCODING:
# in order to use the base64 encoding, the input data has to be in binary

import base64

# first open the image in binary format
image = open('deer.gif', 'rb')

# read the image
image = image.read()

# now if we try to print this image,
# we get all sorts of weird things
# print(image)

# now we have the image in binary data
# now we can encode this data using base64
encoded_data = base64.encodestring(image)

# now if we look at the encoded data
# it contains only [a-zA-Z0-9+/]
# print(encoded_data)

# now that we have the encoded data it can sent over the internet

# now at the receiving end, this is what happens:

# the received encoded_data is decoded first

decoded_data = base64.decodestring(encoded_data)

# now if we look at the data...it again contains all the weird stuff
# print(decoded_data)

# now this decoded data has to written back in binary format
result_image = open('deer_copy.jpg', 'wb')

result_image.write(decoded_data)

# now if you take a look at that result_image, you won't see the image
# but you will an image object description
# print(result_image)












