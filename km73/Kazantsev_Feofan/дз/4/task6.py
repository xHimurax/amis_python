Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 > 8 or x2 > 8 or y1 > 8 or y2 > 8 :
    answer =  "You are a genius. Try once more" 
elif x1 == x2 or y1 == y2 :
    answer = "YES"
elif x1==x2 and y1==y2 :
    answer = "NO"
else :
    answer = "NO"
print(answer)
