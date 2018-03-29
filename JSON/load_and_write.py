
# LOAD AND WRITE


import json


# load the json file and read it
with open('sim.json', 'r') as p:
    input_data = p.read()


# d = json.loads(input_data)
# print(d["a"])
# print(input_data["a"])
# open the file to which the data has to be written
# and start writing
with open('out.json', 'w') as f:
    f.write(input_data)
    print("data written...")
    f.close()


