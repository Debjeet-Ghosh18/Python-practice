name = "Debjeet"
surname = "Ghosh"

# simple string print
intro = "Hi My Self Debjeet, I am pursuing my BSC in Data Science"
print(intro)

print("Hello", name)   # concatenating text with variable

# when we need double quotes inside string → use single quotes outside
introduction = 'Hi, "MySelf Debjeet Ghosh, I am pursuing My BSc in Data Science".'
print(introduction)

# when we need multi-line string → use triple quotes
multiline = '''Hi Debjeet
what are you doing
how was your day
are you going to college tomorrow'''
print(multiline)

# indexing characters from string
print(name[0])  # D
print(name[1])  # e
print(name[2])  # b
print(name[3])  # j
print(name[4])  # e

# using for loop to print each character
print("Using for loop to print each index of name")
for character in name:
    print(character)
