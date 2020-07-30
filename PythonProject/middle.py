num = int(input())
score = list(map(int,input().split))
bignum = max(score)
for i in range (num):
    score[i] = score[i]/bignum *100
r = sum(score)/num
print("%.2f" %r)


d