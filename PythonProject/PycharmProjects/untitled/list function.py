# index() : 리스트 내 특정한 원소의 인덱스를 찾기
list2 = [1,2,3,4,5,6]
print(list2.index(4))
#reverse(): 리스트 함수를 뒤집는 목적
list2.reverse()
print(list2)
#slicing 기법을 이용해 거꾸로 출력도 가능
print(list2[::-1])
#sum() : 리스트 모든 원소의 합(자료형이 같아야함)
print(sum(list2))
#range() : 특정 범위 의 원소 지정
#list 함수와 같이 사용해서 특정 범위 의 원소를 가지는 리스트를 반환
my_range = range(5,10)
list1 = list(my_range)
print(list1)
#all()/any() : 리스트의 모든 원소가 참인경우 / 리스트의 모든 원소가 참이 아닌경우
list3 = [True,False,True]
print(all(list3))
print(any(list3))
#enumerate(): 리스트에서 인덱스와 원소를 함께 추출하는함수
list4 = ['sandy', 'allen', 'pek']
result = list(enumerate(list4)) #tuple 형태로 나옴
print(result)
for i,k in enumerate(list4):
    print('index:' ,i,'/원소 :' , k)
#sorted() 리스트의 원소를 정렬
list4.sort()
print(list4)
#count() 특정한 원소의 개수를 추출
list5= [1,2,3,1,2,3,4,5,6,7,8,9,1,2,3]
print(list5.count(1))
#del() : 리스트의 특정 원소를 제거하는 함수
del list5[1:6]
print(list5)
#insert(): 삽입 시키는 함수
list5.insert(3,15)
print(list5)
#append() 원소의 맨뒤쪽에 집어넣는 함수
list5.append(1234)
print(list5)