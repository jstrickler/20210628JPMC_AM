a = "Bob Smith"
b = 1234
c = 8.2390293

print(a, b, c)

sep = ' '   # default
end = '\n'  # default

print(str(a) + sep + str(b) + sep + str(c) + end )

print(a, b, c, sep=';')
print(a, b, c, sep="/")
print(a, b, c, sep='')
print()

print(a, end="X")
print(b, end="Y")
print(c, end="Z")
print('\n')

print("Values are {},  {}, and {}".format(a, b, c))
print("c is {:.2f}".format(c))

print(f"Values are {a},  {b:4d}, and {c:.2f}")





