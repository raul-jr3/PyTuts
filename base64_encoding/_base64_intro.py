
# base64:
# base64 provides encodin/decoding mechanisms

# this provides base16, base32, base64 algorithms to safely
# encode the values which can be safely sent over the internet

# the data is converted into a representation which contains
# a-zA-Z0-9/+ -> these add up to 64 (26 small case, 26 upper case, 10 numbers,/ and +)

# the data is first converted into it's decimal equivalent(the ascii value)
# these decimal values are converted to their binary equivalent
# equivalent binary values are concatenated
# these are separated into equal sections of 6 bits each
# then these values are converted into their decimal equivalent
# finally these decimals are converted to their base64 equivalent values