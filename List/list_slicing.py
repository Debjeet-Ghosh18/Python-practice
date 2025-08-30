a = [2,45,78,6,7,8,9,5]
print(a)                 # full list

print(a[1:4:1])          # elements from index 1 to 3 → [45, 78, 6]
print(a[-6:-1:2])        # negative index slicing → [78, 7, 9]
print(a[6:-11:-1])       # slicing backwards from index 6 → [9, 8, 7, 6, 78, 45, 2]
