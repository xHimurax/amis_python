import time
x1=int(input("x1="))
y1=int(input("y1="))
x2=int(input("x2="))
y2=int(input("y2="))
a=x1+y1
b=x2+y2
if a%2==0 & b%2==0:
  print("Yes")
if a%2==1 & b%2==1:
  print("Yes")
else:
  print("No")
time.sleep(3)
