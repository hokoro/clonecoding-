A,B,C = map(int,input().split())
Point = 0
if  C<=B:
    Point =-1    
else:
    Point = A//(C-B) +1

print(Point) 