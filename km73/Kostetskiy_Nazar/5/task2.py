a = [int(i) for i in input().split()]

number = 1
for i in range(0, len(a) - 1):

    if a[i] == a[i + 1]:

        number = number + 1

print(number)