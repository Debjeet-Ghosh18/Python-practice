# List inside a list (nested list)
a = [34, 56, 87, 34, [45, 23, 21], 43]

# insert 100 at index 0 of the inner list (a[4])
a[4].insert(0, 100)

print(a)   # inner list becomes [100, 45, 23, 21]
