#WAF to print the len of a list

players =["Vk","GG","YS","RS","ABD","MSD"]

legend =["ST","SG","RD","SG"]

def list_len(list):
    print(len(list))

print(len(legend))
print(len(players))

def print_list(list):
    for item in list:
        print(item,end =" ")

print_list(players)
print()
print_list(legend)
print()
