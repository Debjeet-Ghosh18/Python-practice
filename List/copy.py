# a=[11,22]
# b=[33,44]
# c=a
# print(a,id(a))
# print(b,id(b))
# print(c,id(c))
# a.append(23)
# print(a)
# print(b)
# print(c)


a=[11,22]
b=[33,44]
c=a.copy
print(a,id(a))
print(b,id(b))
print(c,id(c))
a.append(23)
print(a)
print(b)
print(c)
