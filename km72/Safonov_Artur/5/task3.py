list = input("Enter the list of numbers using a 'space' button: ").split()
list1 = []
num = 0

for i in list:
    for j in list:
        if i == j:
            num += 1
    if num == 1:
        list1.append(i)
    num = 0


print("Elements that don`t repeat: ")
print(list1)