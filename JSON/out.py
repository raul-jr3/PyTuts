
import json

with open('sample.json', 'r') as f:
    data = f.read()
    f.close()

d = json.loads(data)
print(d["phoneNumbers"])

# print(data)

# with open('output.json', 'w') as f:
#     f.write(data)
#     f.close()