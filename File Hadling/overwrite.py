f = open("File Hadling\\demo.txt","w")

f.write("I need to keep going")

f.close()

f = open("File Hadling\\demo.txt","r+") #when we overwrite from the begginig then we use a+

f.write("heyee")
print(f.read())