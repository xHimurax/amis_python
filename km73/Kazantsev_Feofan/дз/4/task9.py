Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 > 8 or x2 > 8 or y1 > 8 or y2 > 8 or x1 < 1 or x2 < 1 or y1 < 1 or y2 < 1 :
    answer =  "You are a genius. Try once more" 
elif (x1+1==x2 and y1+1==y2 ) or (x1-1==x2 and y1-1==y2) or (x1+1==x2 and y1-1==y2) or (x1-1==x2 and y1+1==y2) :
    answer = "YES"
elif (x1+2==x2 and y1+2==y2 ) or (x1-2==x2 and y1-2==y2) or (x1+2==x2 and y1-2==y2) or (x1-2==x2 and y1+2==y2) :
    answer = "YES"
elif (x1+3==x2 and y1+3==y2 ) or (x1-3==x2 and y1-3==y2) or (x1+3==x2 and y1-3==y2) or (x1-3==x2 and y1+3==y2) :
    answer = "YES"
elif (x1+4==x2 and y1+4==y2 ) or (x1-4==x2 and y1-4==y2) or (x1+4==x2 and y1-4==y2) or (x1-4==x2 and y1+4==y2) :
    answer = "YES"
elif (x1+5==x2 and y1+5==y2 ) or (x1-5==x2 and y1-5==y2) or (x1+5==x2 and y1-5==y2) or (x1-5==x2 and y1+5==y2) :
    answer = "YES"
elif (x1+6==x2 and y1+6==y2 ) or (x1-6==x2 and y1-6==y2) or (x1+6==x2 and y1-6==y2) or (x1-6==x2 and y1+6==y2) :
    answer = "YES"
elif (x1+7==x2 and y1+7==y2 ) or (x1-7==x2 and y1-7==y2) or (x1+7==x2 and y1-7==y2) or (x1-7==x2 and y1+7==y2) :
    answer = "YES"
elif x1==x2 and y1==y2 :
    answer = "NO"
else :
    answer = "NO" 
print(answer)
