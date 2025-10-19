# Different ways to remove elements from a list
a = [3,5,6,7,8,9,0,6,6,7,8,9,4,4,3,5]
print(a)

a.remove(8)    # remove first occurrence of 8
print(a)

a.remove(6)    # remove first occurrence of 6
print(a)

a.pop(5)       # remove element at index 5
print(a)

# del a       # deletes the whole list (can't use a after this)

del a[2]       # delete element at index 2
print(a)

del a[1:5:1]   # delete elements from index 1 to 4
print(a)

del a[::16]    # delete every 16th element
print(a)
