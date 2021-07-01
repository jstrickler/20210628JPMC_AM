
# business logic  -- DATA
def get_message():
    return "Hello, JPMC world"

m = get_message()

print(m)

# presentation logic -- User Interface
def hello():
    msg = get_message()
    print(msg)

hello()

items = ['a', 'b', 'c']

def update(data):
    local_data = list(data)
    local_data.append('wombat')

update(items)
print(items, '\n')

# mypy
# typing  "type annotations"
def spam(p1, p2, p3):
    print(p1)
    print(p2)
    print(p3)
    print()

spam(1, ['x', 'y'], 48.98)

def ham(*p1):
    print(p1)
    print()

ham()
ham(5)
ham(5, 10, 15, 20, 25, 30)

def jam(p1, p2, *p3):
    print(p1)
    print(p2)
    print(p3)
    print()

jam(5, 6, 7)
jam(8, 42, 99, 23, 23, 5)

def toast(**config):
    print(config, '\n')

toast(country="Western Sahara", animal="Honey Badger", count=3)
toast(brogg=5, cushmakk=22)

def bacon(p1, p2, *, foo, bar):
    print(p1, p2)
    print(foo)
    print(bar)
    print()

bacon(5, 10, foo=12, bar="wombat")
bacon("a", "b", bar=23.83, foo=[1, 2, 3])

def wacky(p1, p2, *p3, p4, p5, **p6):
    pass
















