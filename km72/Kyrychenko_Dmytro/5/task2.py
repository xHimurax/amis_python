a = [int(i) for i in input().split()]
for i in a:
   if a.count(i) == 1: #определяем сколько раз будет входить значение i в список
       print(i)
