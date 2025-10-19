# Demonstrating insert(), append(), extend()

a = [2, 4, 5, 6, 7, 8, "abc"]

a.insert(0, 5656654)   # insert number at index 0
print(a)

a.insert(3, [45, 56, 45])   # insert list at index 3 (as one element)
print(a)

a.extend([34, 56, 77, 7, 8, 8])   # extend adds multiple elements at end
print(a)


# fresh list
a = [2, 3, 4, 5, 6, 7, 8, 9]
print(a)

a.append("abc")   # append adds whole item at end
print(a)

a.extend("degf")   # extend with string → adds each char separately
print(a)

a.extend(["Data Science"])   # extend with list → adds "Data Science"
print(a)
