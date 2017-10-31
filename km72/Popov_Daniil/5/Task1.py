a = [int(a) for a in input('enter list').split()]
number = 0
height = int(input('enter height'))
for i in range(0, len(a)):
    if a[i] >= height:
        number += 1
print(number + 1)
