hour,min = input().split(' ')
hour = int(hour)
min = int(min)
remain =0
if min-45>=0:
    min=min-45
    print(hour,min)
else :  
    if hour-1<0: 
         hour = 23
         remain = 45-min
         min = 60-remain
         print(hour,min)
    else:
        hour=hour-1
        remain = 45-min
        min = 60 -remain
        print(hour,min)
