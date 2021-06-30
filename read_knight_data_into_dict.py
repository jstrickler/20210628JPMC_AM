from pprint import pprint
info = {}

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        # print(name, title, color, quest, comment)
        info[name] = title, color, quest, comment  # add the element
        # info.put(name, new Tuple(title, color, quest, comment));

print(info, '\n')
pprint(info)
print()

for name, data in info.items():
    print(data[0], name)
print()

print(info['Lancelot'][1])




