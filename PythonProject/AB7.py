case = int(input())
plusarr =[]
for i in range(case) :
    A,B = input().split()
    plusarr.append(int(A)+int(B))


for i in range(case) :
  print("Case #%s:%s"%(i+1,plusarr[i]))


    