# create list using list() constructor
a = list((4, 2, "qwerty", 89))
print(a, type(a))   # print list and its type

# access elements by index
print(a[1], a[-3], a[-1], a[2])  
# a[1] = 2, a[-3] = 2, a[-1] = 89, a[2] = "qwerty"

# access 4th character (index 3) of string "qwerty"
print(a[2][3])   # → 'r'
