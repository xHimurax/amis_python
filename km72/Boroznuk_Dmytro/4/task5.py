import time
a=int(input("Enter first_number:"))
b=int(input("Enter second_number:"))
c=int(input("Enter third_number:"))
if (a==b==c):
  print("The quantity of equal numbers:", 3)
elif (b==c!=a) | (b==a!=c) | (a==c!=b): 
  print("The quantity of equal numbers:", 2)
elif a!=b!=c:
  print("The quantity of equal numbers:", 0)
time.sleep(3)
