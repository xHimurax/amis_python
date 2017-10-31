Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> n = int(input())
m = int(input())
k = int(input())
if m == n :
    answer =  "You are a genius. Try once more" 
elif k % n == 0 or k % m == 0 :
    answer = "YES"
else :
    answer = "NO"
print(answer)
