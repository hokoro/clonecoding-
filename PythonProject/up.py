A,B,V = input().split()
count = 0
while V!=0:
    V = V -(A-B)
    count = count+2

print(count)
