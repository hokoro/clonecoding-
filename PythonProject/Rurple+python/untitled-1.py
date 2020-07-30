# -*- coding: utf-8 -*-
a= [10,20,30,40,50,10,10]
b= [80,50,60]
print(a.count(10))
print(a.index(50))
print(a.append(25))
print(a.sort())
a.extend(b)

print(a)

a.insert(3,70)
print(a)
a.remove(10)
print(a)
a.pop(3)
print(a)
a.reverse()
print(a)