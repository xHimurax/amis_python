import time
n=int(input("Введите длинну:"))
m=int(input("Введите ширину:"))
k=int(input("Клітин у частині"))
if n>=m:
  if (k>=m) & (k%m==0):
    print("Yes")
  else:
    print("No")
if m>=n:
  if (k>=n) & (k%n==0):
    print("Yes")
  else:
    print("No")
time.sleep(3)
