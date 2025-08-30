


# n = 15
# m = 7
# ans1 = n+m
# print("Addition of",n,"and",m,"is", ans1)
# ans2 = n-m
# print("Subtraction of",n,"and",m,"is", ans2)
# ans3 = n*m
# print("Multiplication of",n,"and",m,"is", ans3)
# ans4 = n/m
# print("Division of",n,"and",m,"is", ans4)
# ans5 = n%m
# print("Modulus of",n,"and",m,"is", ans5)
# ans6 = n//m
# print("Floor Division of",n,"and",m,"is", ans6)
# print("Floor Division of",n,"and",m,"is", ans6)
#alt + shieft + down arrow ia going to duplicate a line
#with alt + mouse lesft click we can select


# Basic arithmetic operations example

# Take input values
x = float(input("Enter the value of x\n"))
y = float(input("Enter the value of y\n"))

# Ask user which operation to perform
operation = input("Enter the operation which you want to perform (+,-,*,/)\n")

# Perform operation based on user choice
if operation == '+':
    print("The sum of x and y is\n", x+y)
elif operation == '-':
    print("The subtraction of x and y is\n", x-y)
elif operation == '*':
    print("The multiplication of x and y is\n", x*y)
elif operation == '/':
    print("The division of x and y is\n", x/y)

