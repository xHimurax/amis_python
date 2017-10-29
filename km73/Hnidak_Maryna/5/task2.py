'''
Дано список чисел. Порахуйте, скільки в ньому пар елементів, рівних один одному. Вважається, що будь-які два елементи, рівні один одному утворюють одну пару, яку необхідно порахувати.
'''
zirov = [0] *44
k=0
list = [int(e) for e in input("Введіть список - ").split()]
for e in list:
    zirov[e]+=1
for i in range(len(zirov)):
    if zirov[i]>1:
        for e in range(1,zirov[i]):
            k+=e
print(k)
