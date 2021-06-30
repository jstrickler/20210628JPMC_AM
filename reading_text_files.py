
# file_obj = open(file_path, mode)
# file_obj.close()

# modes
#  'r'  read  DEFAULT
#  'w'  write
#  'a'  append
#  'x'  create
#  append 'b' for binary

# mary_in = open(...)
with open('DATA/mary.txt') as mary_in:
    print("File opened OK\n")
# mary_in.close()

with open('DATA/mary.txt') as mary_in:
    for raw_line in mary_in:  # file_obj is a generator
        line = raw_line.rstrip()  # remove trailing whitespace
        print(line)    #  print("blah blah blah")
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    all_contents = mary_in.read()
    print("raw")
    print(repr(all_contents))
    print("normal")
    print(all_contents)
print("-" * 60)

with open('DATA/mary.txt') as mary_in:
    all_lines_with_nl = mary_in.readlines()
    print(all_lines_with_nl)
print("-" * 60)

with open('DATA/mary.txt') as mary_in:
    all_lines_without_nl = [line.rstrip() for line in mary_in]
    print(all_lines_without_nl)
print("-" * 60)

target = 't'
with open('DATA/words.txt') as words_in:
    count = 0
    for line in words_in:
        if line.startswith(target):
            count += 1
print(f"{count} words start with {target}")

target = 'Whig'
with open('DATA/presidents.txt') as pres_in:
    for raw_line in pres_in:
        line = raw_line.rstrip()
        fields = line.split(':')
        if target == fields[-1]:
            print(line)

