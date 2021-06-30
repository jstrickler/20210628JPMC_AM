#  iterables

# MicroSolved
x = 5  # int
s = "foo"  # str
m = [1, 2, 3]   # list
r = {1, 2, 3}   # set
d = {'a': 5, 'b': 10}  # dict
t = 1, 2, 3    # tuple
# OR
t = (1, 2, 3)   # also tuple

person = "Bill", "Gates", "Microsoft", "1955-10-24"

print(type(person))
print(person[0], person[1])

#  var1, var2, ... = iterable

first_name, last_name, product, dob = person
print(person)
print(', '.join(person))
print(first_name, last_name)

values = ['a', 'b', 'c', 'd', 'e', 'f']
x, y, *z = values
print(x, y, z)

x, *y, z = values
print(x, y, z)

*x, y, z = values
print(x, y, z)

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]
print(type(people))
print(type(people[0]))
print(type(people[0][0]), people[0][0])

for person in people:
    #  person = <next value of people>
    print(person[0], person[1])
print('-' * 60)

for first_name, last_name, product, dob in people:
    print(first_name, last_name, dob)
print('-' * 60)

info = [('a', 5), ('m', 32), ('k', 9)]

for letter, number in info:
    print(letter * number)
print()






