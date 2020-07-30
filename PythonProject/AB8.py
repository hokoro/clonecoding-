case = int(input())
arr1 =[]
arr2 = []
ans = []
for i in range(case):
    a,b = map(int,input().split())
    arr1.append(int(a))
    arr1.append(int(b))
    ans.append(int(a)+int(b)) 
    
    
    
for i in range(case) :
    print("Case#%d: %d+%d = %d"%(int(i+1),int(a[i]),int(b[i]),int(ans[i])))