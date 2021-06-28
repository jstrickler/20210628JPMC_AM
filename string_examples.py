s1 = "spam\n"    # \r \f \t \b  \u \U
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''
s5 = r"spam\n"  # raw string

print("It's raining cats and dogs")
print('It is raining "cats" and "dogs"')

print("""It's raining "cats" and "dogs" today""")

sql_query = """
select *
from customers
where state == 'TX'
"""



