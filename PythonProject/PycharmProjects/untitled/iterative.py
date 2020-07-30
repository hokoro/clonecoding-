#반복문: 조건에 부합하는 한 특정한 명령문을 반복적으로 사용하는 구문
#숫자 범위 표현 : range (시작 ,끝)
#continue : 한번의 반복을 뛰어넘을 떄 사용한다
#break : 반복을 탈출하는
count  = 0
for i in "Hello world":
    print(i)
    if i == 'o':
        count+=1

print("o의 개수는 ",count, "개 입니다.")

for i in range(1,10):
    print(i)
sum = 0
list =[1,2,3,4,5]
for i in list :
    if i %2 ==1:
        break #continue
    print(i)

print("합계 :" ,sum)

i = 0
sum = 0

while i<=5 :
    i =i+1
    if i %2 ==1:
        continue
    sum = sum+i

print("합계 : ", sum)