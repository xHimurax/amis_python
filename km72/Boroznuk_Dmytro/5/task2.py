list = input("Введіть список: ").split()
number= 0
for i in range (len(list)):
    i = int(i)
    if (list[i]==list[i-1]) and (i != 0):
      number+=1
      print(number)
