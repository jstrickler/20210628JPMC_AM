fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date"]

with open('fruits.txt', 'w') as fruits_out:
    for fruit in sorted(fruits):
        fruits_out.write(fruit.capitalize() + '\n')


with open('DATA/alice.txt') as alice_in:
    with open('lakme.txt', 'w') as brod_out:
        for line in alice_in:
            replacement_line = line.replace('Alice', 'Lakme')
            brod_out.write(replacement_line)


