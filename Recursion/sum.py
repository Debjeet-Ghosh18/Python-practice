#Write a recursive function to calculate the sum of first n natural numbers

def cal_sum(n):
    if(n==0):
        return 0
    return cal_sum(n-1) + n

print(cal_sum(5))

# Write a recursive function to print all the element in the list 

def print_list(list,indx=0):
    if(indx==len(list)):
        return
    print(list[indx])
    print_list(list, indx+1)

players = ["Vk","RS","MSD"]

print_list(players)




