def cal_sum(a, b):
    sum = a + b
    print(sum)
    return sum

cal_sum(10,12)


def hello(a, b):
    return a*b

sum = hello(5,4)
print(sum)

def print_hello():
    print("Hello")

print_hello()
output = print_hello()
print(output)

## Average of three numbers

def avg_number(a,b,c):
    avg= (a+b+c)/3
    return avg
avg = avg_number(5,5,5)
print(avg)