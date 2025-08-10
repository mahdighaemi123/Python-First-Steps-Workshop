# solution 1
names = input().split()
uniqe_names = set(names)
print(",".join(uniqe_names))

# solution 2
text = input()
names = text.split(" ")
uniqe_names = []

for name in names:
    if name not in uniqe_names:
        uniqe_names.append(name)

result = ""

for name in uniqe_names:
    result = result + name+","

print(result)

# solution 3
text = input()
seperator = " "
uniqe_names = [""]

for index, chr in enumerate(text):
    if chr == seperator:
        if index != len(text) - 1:
            uniqe_names.append("")
    else:
        uniqe_names[-1] += chr

print(",".join(uniqe_names))
