int_value = 1
float_value = 1.23
complex_value = 1+1j
complex_value2 = 1-1j

string_value = 'hello'
string_value2 = "한글도 됩니다"

list_value = [1,2,3]
tuple_value = (1,2,3)
dictionary_value = {1:'true',0:'false',"hello" : "string 도 가능"}

print("정수 ::" , int_value)
print("정수 + 소수 ::" ,int_value +float_value)
print("허수 ::",  complex_value*complex_value2)
print("list ::" , list_value)
print("list[2]:: ",list_value[2])
print("tuple ::",tuple_value)
print("dictionary_value 1 :: ",dictionary_value[1])
print("dictionary ""hello ::",dictionary_value["hello"])