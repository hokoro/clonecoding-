num = int(input())
temp = 0             #몫과 나머지의 합을 저장할 변수
check = num
new_num=0             #
count = 0

while True:
    temp = (num//10)+(num%10)
    new_num = (num%10)*10+temp%10
    count = count+1
    num = new_num
    if new_num == check:
        break

print(count)