hight=(input("Введите рост от 100 до 200:")).split()
n=int(input("Введите рост Пети:"))
number=1
a=0
for i in range (len(hight)):
  a=int(hight[i])
  if a>=n:
    number+=1
    print(number)
