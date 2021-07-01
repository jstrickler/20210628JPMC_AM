counts = {}

with open('DATA/breakfast.txt') as breakfast_in:
    for raw_line in breakfast_in:
        food = raw_line.rstrip()

        if food not in counts:
            counts[food] = 0   # initialize element

        counts[food] += 1   # counts[food] = counts[food] + 1

for food, count in counts.items():
    print(food, count)

