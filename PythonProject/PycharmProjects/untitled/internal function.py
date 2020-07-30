#input() : 사용자가 키보드로 입력받은 데이터를 저장
user_input = input('정수를 입력하세요')
#int() : 정수 자료형 변환
print("제곱 :", int(user_input) ** 2)
#float() : 문자형 정수형을 실수형으로 변환
a = 10
print(float(a))
#max,min () 시퀀스 자료형 중에 가장 큰값을 출력
list = [5,6,3,2,9,8,4,1,7]
print(max(list))
print(min(list))
#bin(),hex() 10진수 -> 2진수 10진수 -> 16진수로 변환
print(bin(128))
print(hex(128))
# 다시 10 진수로 바꿀떄
print(int('0xe6',16))
# round : 반올림 하는 함수 이다 (소수점 아래는 양수 소수점 위는 음수로 index 를 표현)
print(round(127.865,-1))
#type(): 자료형의 종류를 알려주는 함수 이다
int = 1
str='문자열'
list = [1,2,3]
dict = {'apple': '사과'}
print(type(int))
print(type(str))
print(type(list))
print(type(dict))