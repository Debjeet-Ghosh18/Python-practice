# Example 1: Multiplying a string by numbers
a, b = 2, 3
txt = "@"
print(a * txt * b)  # "@@" repeated 2 times -> "@@" then repeated 3 times -> "@@@@@@"



# Example 2: Concatenating string and multiplying
a, b = "2", 3
txt = "@"
print((a + txt) * b)  # "2@" repeated 3 times -> "2@2@2@"



# Example 3: Operator precedence in arithmetic
a, b = 2, 3
c = 5
print(a + b * c)  # Multiplication first: 3*5=15, then add 2 -> 17



# Example 4: Multiplying floats
a, b = 1.5, 9
c = a * b
print(c)  # 1.5 * 9 = 13.5



# Example 5: Floor division and true division
a, b = 5.0, 2
c = a // b
print(c, a / b)  # Floor division: 5.0//2=2.0, normal division: 5.0/2=2.5



# Example 6: Modulo operation with positive numbers
a = 5
b = 2
c = a % b
print(c)  # 5 % 2 = 1 (remainder when 5 divided by 2)



# Example 7: Modulo operation with negative numbers (both negative)
a = -5
b = -2
c = a % b
print(c)  # -5 % -2 = -1 (remainder has the same sign as divisor)



# Example 8: Modulo operation with negative dividend
a = -5
b = 2
c = a % b
print(c)  # -5 % 2 = 1 (remainder has the same sign as divisor)




# Example 9: Modulo operation with negative divisor
a = 5
b = -2
c = a % b
print(c)  # 5 % -2 = -1 (remainder has the same sign as divisor)




































































































































