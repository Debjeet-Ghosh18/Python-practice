example = set() # Empty Set


### Add method
example.add(1)
example.add(2)
example.add(3)
example.add("hello")
example.add(5)

### Remove method

example.remove(5)

### Clear Method 
example.clear()

print(example)


### Pop Method
colletion = {1,2,3,4,5,6,7,7,8}

print(colletion)
print(len(colletion))

print(colletion.pop())
print(colletion.pop())
print(colletion.pop())
print(colletion.pop())

print(type(colletion))
print(colletion)

### UNION Method combines both set value and return new

set1 = {1,2,3}
set2 = {3,4,5}

print(set1.union(set2))
print(set1)
print(set2)

### Intersection Method combines common value and returns new 
print(set1.intersection(set2))
























