a = int(input("Введите число а :"))
b = int(input("Введите число b :"))
c = int(input("Введите число c :"))

if a > b & b > c  :
    print (c)
elif b > c & c > a :
    print (a)
elif c > a & a > b :
    print (b)