a=[]
n = int(input("количество людей "))
x = int(input("рост Пети "))
if x>200 or x<100:
    x = int(input("Заново введите рост Пети "))
j=1
for i in range(n):
    new_element = int(input("Рост однокласника "))
    if x>200 or x<100:
        x = int(input("Заново введите рост одноклассника "))
    a.append(new_element)
    if(a[i]>x):
        j=j+1
print("Петя будет в строю "+(str)(j))
