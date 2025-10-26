# Working with index, count, reverse, sort

a = [3,4,5,6,7,8,9,0,4,5,6,3,5,6,7,8,8]
print(a)   # print list

print(a.count(5))   # how many times 5 appears
print(a.index(3))   # first index of value 3

a.reverse()   # reverse the list
print(a)

a.sort()   # sort ascending
print(a)

a.sort(reverse=True)   # sort descending
print(a)
