case = int(input())
arr = list(range(case))
arr = list(map(int,input().split()))
arr.sort()
min = arr[0]
max = arr[case-1]
print(min,max)

