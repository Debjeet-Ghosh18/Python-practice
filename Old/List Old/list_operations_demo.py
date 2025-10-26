"""
List slicing examples
"""
a = [2,7,4,5,22,89,12]
print(a)
print(a[1:6:2])    # elements from index 1 to 5 with step 2
print(a[-6:-1:2])  # negative index slicing
print(a[5:-11:-2]) # slicing backwards
print(a[3:7])      # elements from index 3 to 6


"""
Insert method
"""
a = [3,11,56,67,45,90,"abc"]
print(a)
a.insert(1,100)          # insert at index 1
print(a)
a.insert(5,[11,67,56])   # insert a list at index 5
print(a)


"""
Insert, Append
"""
a = [2,8,1]
print(a)
a.insert(-1,200)         # insert before last element
print(a)

a.append(100)            # append number
print(a)
a.append(True)           # append boolean
print(a)
a.append([56,"qwerty"])  # append list as one element
print(a)


"""
Append vs Extend
"""
a = [22,66,11,99]
print(a)
a.append([11,22,33])     # appends whole list as single element
print(a)
a.extend([11,22,33])     # extends by adding each element separately
print(a)


"""
Append string vs Extend string
"""
a = [3,5,6,7]
print(a)
a.append("aabc")         # append whole string as one element
print(a)
a.extend("abc")          # extend adds characters separately
print(a)
a.extend(["abc"])        # extend with list → adds "abc" as one element
print(a)


"""
Clear, Pop, Remove
"""
# a.clear()              # clears all elements
# print(a)

# a.pop(10)              # pop element at index 10 (error if not exists)
# print(a)
# a.pop(1)               # pop element at index 1
# print(a)

# a.remove(21)           # remove first occurrence of value
# print(a)
# a.remove(89)
# print(a)
# a.remove(2)
# print(a)


"""
Nested list operations
"""
a = [2,7,4,[22,33,44],78]
print(a)
a[3].insert(2,100)       # insert inside nested list
print(a)
a[3].remove(22)          # remove from nested list
print(a)


"""
Reverse, Sort, Count, Index
"""
# a = [2,7,4,5,3,9,2,2,2,2,5,7,5,6,1]
# print(a)
# a.reverse()             # reverse order
# a.sort()                # sort ascending
# print(a)
# a.sort(reverse=True)    # sort descending
# print(a)
# print(a.count(7))       # count occurrences of 7
# print(a.index(2))       # first index of 2


"""
Copy vs Reference
"""
a = [11,22]
b = [33,44]
c = a.copy()             # makes a separate copy of list
print(a,id(a))
print(b,id(b))
print(c,id(c))

a.append(45)             # change in a does not affect c
print(a)
print(b)
print(c)
