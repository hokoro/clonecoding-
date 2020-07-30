#시퀀스 자료형 : 문자열 ,리스트 튜플 등에 index 를 가지고 있는 자료형이다
# 순서를 가지면서 많은 양의 데이터를 포함하면서

string = "hello world"
list = ['h','e','l','l','o',' ' ,'w','o','r','l','d']
tuple =('h','e','l','l','o',' ' ,'w','o','r','l','d')
print(string)
print(list)
print(tuple)
# 마찬가지로 indexing slicing 이 다 적용된다
print(string[0:5])
print(list[0:5])
print(tuple[0:5])

for i in string:
    print(i)
for i in list:
    print(i)
for i in tuple:
    print(i)

#operator 사용 가능
string1 ="hello"
string2 =" world"

print(string1+string2)
#len 시퀀스 자료형의 길이를 확인하는 함수
print(len(string1+string2))
#조건문이나 반복문으로 활용 가능
print(4 in list)
if 5 in string:
    print("true")