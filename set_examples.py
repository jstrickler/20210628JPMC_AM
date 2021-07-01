
with open('DATA/breakfast.txt') as breakfast_in:
    foods = [food.rstrip() for food in breakfast_in]

print("foods:", foods)
unique_foods = set(foods)
print("unique foods:", unique_foods)
print()

colors1 = ['red', 'blue', 'purple', 'blue', 'orange', 'black', 'white']
colors2 = ['green', 'orange', 'white', 'purple', 'pink', 'ecru', 'purple']

s1 = set(colors1)
s2 = set(colors2)

s1.add('blue')
s1.add('yellow')

print("s1:", s1, '\n')
print("s2:", s2, '\n')

print("both:", s1 & s2)  # intersection
print("just one:", s1 ^ s2)   # xor
print("either:", s1 | s2)  # union
print("just s1:", s1 - s2)
print("just s2:", s2 - s1)






