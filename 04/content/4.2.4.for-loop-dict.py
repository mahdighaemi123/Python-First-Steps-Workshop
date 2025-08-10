# Dictionaries:
d = {
    "mahdi": 20,
    "ali": 21
}

print(d.items())
# iterate on all keys
for key in d:
    print(key, d[key])

# iterate on all key value perires
# .items() will retuen list of key value pair [(key1,value1),...]
for name,age in d.items():
    print(name,age)