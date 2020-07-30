#문자열 자료형 뒤집기 slice 활용
str = "helloworld"
print(str[::-1])
#len 문자열의 길이 출력 ,뿐만 아니라 python 의 자료형 길이를 출력
print(len(str))
#isalpha(): 특정한 문자열이 오직 문자 로만 이루어져 있는지 확인
print(str.isalpha())
#isdigit(): 특정한 문자열이 숫자로만 이루어져 있는지 확인
str = '123123'
print(str.isdigit())
#isalnum(): 특정한 문자열이 문자와 숫자로만 아루어져 있는지 확인
str = 'asd123'
print(str.isalnum())
#join() : 여러개의 문자열을 구분자와 함께 합치는 함수
list = ['hello','world','홍길동']
print('.'.join(list))
#sorted(): 문자열 정렬 함수
list = sorted(str)
print(list)
#내림차순 정렬
list = sorted(str,reverse =True)
print(list)
#split 문자열 분리 함수
str = "I wanna watch a movie"
list = str.split(' ')
print(list)
#find() 문자열의 서브 문자열을 찾는 아 위치를 반환하는 함수
print(str.find('asd', 0) ) # 0 index 위치 이후에 asd 를 찾는다
#upper , lower : 문자열을 대문자 와 소문자로 바꾸는 함구
str = 'Hello World'
print(str.upper())
print(str.lower())
#strip() 좌우로 특정한 문자열을 제거 하는 함수
str = "tt hello world tt"
print(str.lstrip()) # 왼쪽에 있는 데이터만 없애고 싶을때
print(str.rstrip()) # 오른쪽에 있는 데이터만 없애고 싶을떄
print(str.strip('tt')) # 아무런 데이터를 안넣으면 공백을 제거하는 함수
#eval() : 문자열 수식을 계산하는 함수
exp = '203+450 * 3 -265'
print(eval(exp))
