### WAP TO CHECK IF A LIST CONTAINS A PALINDROME OF ELEMENTS

list = [1,2,3,2,1]
print(list)

copy_list1 = list.copy()
copy_list1.reverse()
print(copy_list1)

if(list == copy_list1):
    print("A LIST CONTAINS A PALINDROME OF ELEMENTS")
else:
    print("A LIST DOES NOT CONTAINS A PALINDROME OF ELEMENTS")

