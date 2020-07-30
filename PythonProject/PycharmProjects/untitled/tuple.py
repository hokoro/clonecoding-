#튜플은 리스트와 비슷한 자료형이다 (변경 불가 리스트 라고 생각하면 된다)
#튜플역시 많은 양에 데이터를 담을수 있다

tuple =(1,2,3)
for i in tuple:
    print(i)

# 리스트 를 튜플에 원소를 집어 넣을수가 있다
list1 = [1,2,3]
list2 = [4,5,6]

tuple = (list1,list2)
print(tuple)
print(tuple[0][1])
#지정된 원소들은 바꿀수 없지만 tuple 의 원소가 list 의 경우의 원소 각각은 변경이 가능하다
tuple[0][1] = 7
print(tuple[0][1])

# indexing slicing 둘 다 가능하다
tuple = (1,2,3,4,5,6,7,8,9)
print(tuple[0:5])
#연산도 가능 하다
print(tuple[0:5]*3)