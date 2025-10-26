i = 1
while i<=5:
    print(i)
    i += 1
    if(i==4):
        break
print("End of the Loop")

tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

X = int(input("Enter the value of X: "))

i = 0
while i < len(tuple):
    if(tuple[i] == X):
        print("Found at indx",i)
        break
    else:
        print("Finding")
        i += 1

j=0
while j <= 5:
    if(j==3):
        j+=1
        continue # It acts as skip
    print(j)
    j+=1

j=0
while j <= 20:
    if(j%2==0):
        j+=1
        continue # It acts as skip
    print(j)
    j+=1

j=0
while j <= 20:
    if(j%2!=0):
        j+=1
        continue # It acts as skip
    print(j)
    j+=1










