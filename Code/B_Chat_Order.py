n = int(input())
name_list = {}

for i in range(n):
    x = input()
    name_list[x] = x
    if not x in name_list[x]:
        name_list[x] = x 
    else:
        name_list.pop(x)
        name_list[x] = x 
name_list = reversed(name_list.keys())    
print(*name_list , sep="\n")