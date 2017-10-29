massive = []
n = int(input("Enter the number of element in massive: "))
for i in range(n):
    new_element = int(input("Enter an element: "))
    massive.append(new_element)
for i in range(n):
    if massive.count(massive[i]) == 1:
        print(massive[i], end = ' ')


input()
