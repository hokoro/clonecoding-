# lamda 키워드를 이용해서 매개변수를 지정하고 출력을 한다
# 함수를 더욱 짧게 사용할수가 있다
add = lambda x,y : x+y
print(add(1,2))
#map(): 다수의 원소에 대한 함수의 결과를 한번에 얻을수 있도록 도와주는 문법
list1 = [1,2,3,4,5,6]
list2 = [6,7,8,9,10,11,12]
my_function = lambda  a,b : a+b
#map 과 lambda 는 같이 사용할수도 있음
result = map(my_function,list1,list2)
print(list(result))