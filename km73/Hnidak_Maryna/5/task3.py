'''
Дано список. Виведіть ті його елементи, які зустрічаються в списку тільки один раз. Елементи потрібно виводити в тому порядку, в якому вони зустрічаються в списку.
'''
'''
List=input("GGG")
isError=False
N=List.split()
A=''.join(N)
for symbol in A:
    if A.find(symbol)!=-1:
        isError=True
        break
    '''
'''
list = input("GGG")
data=list.split()
for i in data:
     if data.count(i) == 1:
           data.remove(i)
print (data)
''''''
list = input("CCC - ")
data = list.split()
i = len(data)-1
while i>=0  :
     if data.count(data[i]) != 1:
        data1=data.remove(data[i])
        i = i-1
for i in data:
     if data.count(i) == 1:
        data2=data.remove(i)
data3 = [i for i in data1 if i not in data2] 
print (data3)''''''
list= input("Введіть зріст інших учнів - ")
list1= input("Введіть зріст Петі - ")
patter="0123456789"
isError=False
N=list.split()
H="".join(N)
l=list1.split()
h=''.join(list1)
print(h)
i=-1
if int(h)<= 200:
    for symbol in H:
        if patter.find(symbol)==-1:
            isError=True
            break
    if not isError:
        for k in h:
            if patter.find(k)==-1:
                isError=True
                break
        if not isError:
            for i in h:
                i+="1"
                print(N.index(h+i)+2)
                
        else:
            print("Error")
else:
    print("Error")
    ''''''
arr = [int(i) for i in input("Введіть зріст інших учнів - ").split()]
N=len(arr)-1
i=0
for j in range(i+1,N):
    if arr[i] != arr[j]:
        print(arr[l])'''
data=[int(i) for i in input("Введіть список - ").split()]
rm = []
for k in data:
    if data.count(k) == 1:
        print(rm.append(k))
for x in rm:
    print(data.remove(x))
