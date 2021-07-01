
# local -> global -> builtin

animal = "wombat"   # global variable


def spam():
    x = 5   # local variable
    print("in spam(): x is", x)
    print("in spam(): animal is", animal)


spam()

# print("in main: x is", x)

