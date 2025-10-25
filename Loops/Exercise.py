# # 1. print number from 1 to 100
# i = 1
# while i<=100:
#     print(i)
#     i += 1

# # 2. Print numbers 100 to 1
# i = 100
# while i>=1:
#     print(i)
#     i -= 1

# # 3. print the multiplication table of number 1 

# n = int(input("Enter the value of n :"))
# i=1
# while i<=10:
#     print(f"{n} x {i} = {n * i}")
#     i += 1


# 4.Print the elements of the following list using a loop:[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# indx = 0
# while indx < len(nums):
#     print(nums[indx])
#     indx += 1
    

# 5.Search for a number x in this tuple using a loop:(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

X = int(input("Enter the value of X: "))

i = 0
while i < len(tuple):
    if(tuple[i] == X):
        print("Found at indx",i)
    else:
        print("Finding")
        i += 1













