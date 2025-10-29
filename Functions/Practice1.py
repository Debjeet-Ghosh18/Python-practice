n = int(input("Enter the value of n: "))

def check(n):
    if(n % 2 == 0):
        print("EVEN")
    else:
        print("ODD")
    return check

check(n)