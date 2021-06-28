actor = "Chris Hemsworth"

print(type(actor), len(actor))

print(actor.upper(), actor.lower())

print(actor.count('h'))
print(actor.count('worth'))
print(actor.lower().count('h'))
print(actor.startswith("Chris"))
print(actor.startswith("Liam"))

print(actor.find('Chris'))
print(actor.find("worth"))
print(actor.find("Liam"))

print(actor.replace("Chris", "Liam"))

line = "Joe;Blow;Houston;TX"
fields = line.split(';')
print(fields)

line = "This is      a           test"
print(line.split())

s = "       All my exes live in Texas        "
print("|" + s.lstrip() + "|")
print("|" + s.rstrip() + "|")
print("|" + s.strip() + "|")
print()

s = "xxyyxyxyxxxxxyyAll my exes live in Texasxyyyyyyyyyxyyxxxxxxxxxxxxy"
print("|" + s.lstrip("xy") + "|")
print("|" + s.rstrip("xy") + "|")
print("|" + s.strip("xy") + "|")
print()








