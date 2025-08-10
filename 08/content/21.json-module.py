# json module:
# module for woeking with jsons(dicts in python)

import json

data = {
    "run": True,
    "sleep": False,
}

# dict to string
data_str = json.dumps(data)

with open("my_data.json", "w", encoding="utf8") as f:
    f.write(data_str)

with open("my_data.json", "r", encoding="utf8") as file:
    data_str = file.read()

# string to dict
data = json.loads(data_str)

print(data)
print(type(data))
