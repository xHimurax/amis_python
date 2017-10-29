b=True
number=1
while b:
    s = input("Введіть послідовність чилел\n")
    a = s.split()
    n=len(a)
    b=False
    for i in range(n):
       a[i]=int(a[i])
       if a[i]>200:
           b=True
           print("Ріст більший за 200 у "+str(i+1)+" по списку")
    
ss = int(input("Введіть число "))

for i in range(n):
    if ss<=a[i]:
        number=number+1
print(number)
