num = []
max_index = 0
max_num = 0
for i in range(9) :
    num.append(int(input())) 

for i in range(9) :
    if num[i]>max_num:
        max_num = num[i]
        max_index = i
print(max_num)
print(max_index+1)