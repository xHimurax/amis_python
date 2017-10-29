row=input("height of each: ").split()
petya=input("height of Petya: ")
row.sort()
row.reverse()
list=[]
for i in range(len(row)-1):
    if (petya <= row[i-1]) and (petya > row[i]):
        list.append(petya)
    list.append(i)
print("Petya is on the line:",list.index(petya)+1)