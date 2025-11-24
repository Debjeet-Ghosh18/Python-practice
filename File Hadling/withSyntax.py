with open("File Hadling\demo.txt","r") as f:
    data = f.read()
    print(data)

with open("File Hadling\demo.txt","w") as f:
    f.write("New Data")