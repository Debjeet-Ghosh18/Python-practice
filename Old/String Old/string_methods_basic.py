a = "hello,debJeet "
print(a.upper())   # convert to uppercase
print(a.lower())   # convert to lowercase

# rstrip() → removes given characters from the right end of string
b = "!!Debjeet !!!!!!!"
print(b.rstrip("!"))   # remove trailing '!'
print(b.rstrip("!"))   # same again
print(b.rstrip("j"))   # no effect, because 'j' is not at the end

# strip() → removes spaces (or given chars) from both ends
c = "  Debjeet  "
print(c.strip())   # removes extra spaces
