# name ="Debjeet"
# print(len(name))

# fruit ="Mango"
# fruit1=len(fruit)
# print("Mango is a",fruit1,"letter Word")
# print(fruit[0:5])#Mango
# print(fruit[1:4])#ang here first 1 is inclube last 4 is not: Same for the others
# print(fruit[2:5])#ngo
# print(fruit[-3:-1])#5-3=2 to 5-1=4 so it is 2:4 answer will be ng
# print(fruit[-2:-1])#g
# print(fruit[-4:-2])#an

# nm="harrygdg"
# print(len(nm))
# print(nm[-4:-2])#yg
name = "Debjeet"
print(len(name))   # length of string

fruit = "Mango"
fruit1 = len(fruit)
print("Mango is a", fruit1, "letter Word")

# string slicing
print(fruit[0:5])   # Mango → from index 0 to 4
print(fruit[1:4])   # ang → index 1 to 3
print(fruit[2:5])   # ngo → index 2 to 4

# negative indexing slices
print(fruit[-3:-1])   # ng  → index -3 to -2
print(fruit[-2:-1])   # g   → only index -2
print(fruit[-4:-2])   # an  → index -4 to -3

nm = "harrygdg"
print(len(nm))        # length = 8
print(nm[-4:-2])      # yg → index -4 to -3
