from mortgage.db import johnlib
import os
import sys

# from framework1.utils.foo import blah
# from framework2.utils.foo import bar


johnlib.spam()
johnlib.ham()

# johnlib._toast()  # naughty programmer!!
print(johnlib.ANIMALS[-1])

print(os.getenv("PYTHONPATH"))
print()
for path in sys.path:
    print(path)
print()

print(sys.prefix)


