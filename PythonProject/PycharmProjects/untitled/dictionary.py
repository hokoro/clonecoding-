dict = { }
dict['안녕']  = 'Hello'
dict['기적'] = 'Miracle'
dict['노력'] = 'effort'
print(dict)
#특정 데이터 부분에서 수정이 가능하다
dict['안녕'] = "hi"
#사전에서 키값만 가져올떄
keys = dict.keys()
print(keys)
#사전에서 값만 가지고 나올떄
values = dict.values()
print(values)
#사전의 키를 리스트로 바꾸고 싶을때
key_list = list(keys)
print(key_list)
#사전의 값을 리스트로 바꾸고 싶을때
value_list = list(values)
print(value_list)
#특정한 키값의 존재 여부를 확인
if '노력' in dict:
    print("노력이 존재 합니다 ")
#사전의 길이
print("사전 자료형의 길이", len(dict))
print(dict)
#i = index k = key  dict[k] = value
for i ,k in enumerate(dict) :
    print("[인덱스: ",i,"] 한글:",k, "/ 영어:",dict[k])
#원소 삭제
del dict['기적']
#모든 원소 삭제
dict.clear()


