import sqlite3

file_name = "wombats.txt"
try:
    with open(file_name) as file_in:
        pass
except FileNotFoundError as err:
    print(err)
except (PermissionError, IsADirectoryError) as err:
    print(err)

values = [1, 3.9, 0, 7, 6, 18, 0]
try:
    print(values[99])
except IndexError as err:
    print(err)

for v in values:
    try:
        result = 22 / v
    except ZeroDivisionError as err:
        print(err)
    else:
        print(result)

conn = None
try:
    conn = sqlite3.connect("barf.db")
except sqlite3.DatabaseError as err:
    print(err)
    sys.exit()
else:
    pass  # access DB here ...
finally:
    if conn is not None:
        conn.close()







print("All done.")
