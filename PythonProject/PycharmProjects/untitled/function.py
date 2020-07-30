#함수 : 특정한 입력을 받아서 특정한 출력을 하는 모듈
#함수를 이용하면 특정한 소스코드에 반복을 줄여주는 역할을 한다
#return 을 사용해서 데이터의 결과를 반환
# 함수 내에서 결과를 바로 출력도 가능
# 가변인자 함수의 매개변수가 가변적일수 있을 떄 사용
# 전역 변수- 어디든 사용가능 변수
# 지역변수 - 한 함수 즉 지역내에서 만 사용가능 한 함수
# 파이썬 함수의 특징 반환값이 여러개 이 있을수 있다.
def add(a,b):
    return a+b
def add2(c,d):
    print(c+d)
def function(*data):
    print(data)
def function():
    a = 5
    b= [1,2,3]
    return a,b
ans1 = input().split(' ')
x= int(ans1[0])
y= int(ans1[1])
print(add(x,y))
print(add2(x,y))

#function(1,2,3)
a,b =function()

print(a)
print(b)

