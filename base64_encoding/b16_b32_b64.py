
import base64

a = "escn"

# the base16 encoding results in only hexadecimal values
result_16 = base64.b16encode(a)
print(result_16)

# the base32 encoding results in all upper case alphabets and numbers from 2-7
result_32 = base64.b32encode(a)
print(result_32)

result_64 = base64.b64encode(a)
print(result_64)


# '=' are added as padding values

decoded_result16 = base64.b16decode(result_16)
print(decoded_result16)

decoded_result32 = base64.b32decode(result_32)
print(decoded_result32)

decoded_result64 = base64.b64decode(result_64)
print(decoded_result64)








