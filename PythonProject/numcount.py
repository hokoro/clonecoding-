from collections import Counter
A= int(input())
B= int(input())
C= int(input())


num= A*B*C

num = str(num)
for i in range(0,10) :
    print(num.count(str(i)))


