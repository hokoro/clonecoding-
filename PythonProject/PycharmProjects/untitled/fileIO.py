#해당 프로그램을 실행하면서 파일을 만들거나 파일을 가져와 서 파일을 열어 볼수가 있음
#open() : 파일을 특정한 모드로 여는 함수 읽을떄는 'r'  쓸때는 'w' 을 사용
#f = open("input.text",'r',encoding="UTF-8")
#f.seek(9) # 파일의 시작위치를 자정해줌 byte 단위
#read()  파일 객체로 부터 모든 파일의 내용을 읽어 온다
#data = f.read()
#print(data)

#f.readline() : 파일을 한줄씩 읽는 함수
#count = 0
#while count < 3:
   #data = f.readline()
    #count = count +1
   # print("%d번쨰 줄: %s" %(count,data),end=' ')

#readlines() : 전체 내용을 담는 함수
#list1 = f.readlines()
#for i,data in enumerate(list1):
    #print("%d번째 줄 : %s" %(i+1,data),end = '')
#print(list)
#f.close()

#with open("input.text","r",encoding="UTF-8") as f:
 #   list1 = f.readlines()
  #  for i,data in enumerate(list1):
    #    print("%d번째 줄 : %s" % (i + 1, data), end='')

def process(filename):
    with open(filename,"r") as f:
        dict1 = []
        data = f.read()
        for i in data:
            if i in dict1:
                dict1[i]+= 1
            else:
                dict1[i] = 1
    return dict1

dict1 = process("input.text")
dict1 = sorted(dict.items(),key = lambda a:a[1],reverse = True)
print(dict1)
