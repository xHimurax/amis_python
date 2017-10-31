a=(input("list:")).split()
number = 0
for i in a:
    for j in a:
        if i == j:
           number=number +1
    number=number - 1
print (number / 2)
