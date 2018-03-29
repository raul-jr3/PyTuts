
import json


# to load an external file, use the json.load function and specify the filename
# data = json.load(open('sample.json'))
#
# output_data = json.dumps(data)

with open('out.json', 'r') as f:
    data = f.read()
    f.close()

# json.dumps(data)


# print(data)

# d = json.loads(data)
#
# print(d)
# print(output_data)

# print(data)