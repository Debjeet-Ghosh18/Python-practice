### RANDOM PASSWORD GENERATOR

import random
import string

# print(type(string.ascii_letters))
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.ascii_letters)
# print(string.punctuation)
# print(string.digits)
# val = random.choice([1,2,3])

pass_len = 12
charValues = string.ascii_letters + string.punctuation + string.digits

#List Comprehension
# res = "".join([random.choice(charValues) for i in range(pass_len)])
# print(res)

password = ""
for i in range(pass_len):
   password += random.choice(charValues)

print("Your Random Password is ",password)


























