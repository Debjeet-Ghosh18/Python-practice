# Example: list assignment vs copy

# Original lists
a = [11, 22]
b = [33, 44]

# Wrong way: this just stores the "copy function" reference, not a copied list
c = a.copy    

print(a, id(a))   # print list a and its memory id
print(b, id(b))   # print list b and its memory id
print(c, id(c))   # c is not a list yet, it’s a function reference

# Append an element to 'a'
a.append(23)

print(a)   # 'a' gets updated
print(b)   # 'b' remains same
print(c)   # 'c' still shows function reference, not list
