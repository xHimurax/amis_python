import time
a=int(input("Enter first_number:"))
b=int(input("Enter second_number:"))
c=int(input("Enter third_number:"))
if a<b and a<c:
  print("The minimum is", a)
elif b<a and b<c:
  print("The minimum is", b)
elif c<b and c<a:
  print("The minimum is", c)
elif (a==b)<c:
  print("The minimum is", a)
elif (b==c)<a:
  print("The minimum is", b)
elif (a==c)<b:
  print("The minimum is", a)
else:
  print("a=b=c")
time.sleep(3)
