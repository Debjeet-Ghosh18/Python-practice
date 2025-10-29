# Print the elements of the follwing list using a loop
# [1,4,9,16,25,36,49,64,81,100]


numbers = [1,4,9,16,25,36,49,64,81,100]

for hello in numbers:
    print(hello)

x=36

idx = 0
for el in numbers:
    if(el == x):
        print("Found at idx",idx)
    idx += 1





