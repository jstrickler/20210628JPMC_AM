i = 0
while i < 5:
    print(i)
    i += 1
print()

# while EXPR:   uncommon

while True:
    state = input("Enter a state abbreviation: ")
    if state == 'q':
        break  # exit loop
    if state == '':
        print("Please enter a 2-letter state abbreviation")
        continue   # jump to top of loop
    if len(state) != 2:
        print("Abbreviation must be 2 letters")
        continue
    if not state.isalpha():
        print("Abbreviation must be letters only")
        continue
    if not state.isupper():
        print("Abbreviation must be upper case")
        continue
    print("You entered", state)
