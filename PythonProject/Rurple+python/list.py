# -*- coding: utf-8 -*-

a = [3.5,4.3,2.3,3.5,3.2,4.5]
# 리스트 전체 출력
print(a)
#특정 인덱스 의 값을 출력 
print(a[0])
print(a[1])
print(a[2])
print(a[3])

#반복문을 이용한 접근
sum =0
for i in a :
    sum += i

print("평균점수: " , sum/len(a) )

b=[[90,95,83,40,30,20,19,48,39,59],[48,53,64,76,58,34,55,85,96,85]]

sum = 0 
english  = b[0]
for i in english :
    sum+=i

print(sum/len(english))

sum = 0
math = [1]

for i in math:
    sum = sum + i

print(sum/len(math))