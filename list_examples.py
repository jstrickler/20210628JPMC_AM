list1 = list()   # new, empty, list
list2 = ['red', 'purple', 'orange']   # literal list
list3 = []   # new, empty, list

cities = ['Durham', 'Plano', 'Seattle', 'New York', 'Chicago', 'Scottsdale']
print(cities[0], cities[3])
print(cities, '\n')

cities.append('Tampa')
print(cities)

more_cities = ['Winchester', 'Cleveland', 'Metairie']
cities.extend(more_cities)
print(cities)

cities.insert(0, 'London')
print(cities)
cities.insert(5, 'Emerald City')
print(cities)

# add to list:
# LIST.append(obj)  LIST.extend(iterable)  LIST.insert(pos, obj)
cities[-1] = "New Orleans"

print(cities)
cities[2] = 'Arlington'
print(cities)

del cities[6]
print(cities)

x = 5
del x

city = cities.pop()   # remove and return last element
print(city)
print(cities)

cities.remove('Tampa')
print(cities)

#  remove from list:
#  del LIST[pos]   LIST.pop(pos=-1)  LIST.remove(value)

#  list tuple str bytes
print(cities[0], cities[4], cities[-1], cities[-3])

print(cities[0:4])   # cities[0] through cities[3]
print(cities[3:6])   # [3], [4], [5]

s = "wombat"
print(s[0:2], s[-3:len(s)], s[2:5].upper())
print(s[:2], s[-3:], s[2:5].upper())
print(cities[-4:])
print(cities[:3])
print(cities, '\n')

for city in cities:
    # city = <next-value-of-cities>
    if len(city) > 6:
        print(city)
print()

s = "abc"
for letter in s:
    print(letter.upper())
print()

# for VAR in ITERABLE:
#     ...

empty_list = []
for x in empty_list:
    print("PYTHON IS GREAT!")

nums = [800,80,1000,32,255,400,5,5000]
print(cities)
print(nums)
print()

print(len(nums), len(cities))
print(min(nums), max(nums), min(cities), max(cities))
print(sorted(nums), sorted(cities))
print()

rnums = reversed(nums)
rcities = reversed(cities)
print(rnums)
for num in rnums:
    print(num)
print()

print(rcities)
for city in rcities:
    print(city, end=', ')
print('\n')

states = ['NC', 'AZ', 'NY']
capitals = ['Raleigh', 'Phoenix', 'Albany']

caps = zip(states, capitals)
print(caps)
for state, capital in caps:
    print(state, capital)

print(list(zip(states, capitals)))
print(list(reversed(nums)))
print()

for i, city in enumerate(cities):
    print(i, city)
print()

e = enumerate(cities)
print(list(e))
print(list(e))
print()

for city in 'Durham', 'Dallas', 'Des Moines', 'Houston', 'Winchester':
    print(city, city in cities)
print()

print(['foo'] * 5)
print(['a', 'b', 'c'] + [4, 5, 6])


i = 0
while i < 10:
    print("Pew! Pew!")
    i += 1
print()


# range(STOP)    range(START, STOP)   range(START, STOP, STEP)
for i in range(10):
    print("Pew! Pew! Pew!")
print()

for i in range(1, 11):
    print(i)
print()

for i in range(5, 101, 5):
    print(i, end=' ')
print('\n')
























