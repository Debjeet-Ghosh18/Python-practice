n=5
fact = 1
for i in range(1, n+1):
    fact *= i
print(fact)


def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)
    return factorial

factorial(6)



def convert(USD):
    INR = 83*USD
    print(USD,"USD =",INR,"INR")
    return convert

convert(1)