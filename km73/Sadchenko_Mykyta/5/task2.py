list=input("list: ").split()
n=0
for i in list:
    n+=((list.count(i)*(list.count(i)-1))/2)/list.count(i)
print("couples:",int(n))