massive = []
n = int(input("Lenght of the massive: "))
for i in range(n):
    new_element = int(input("Enter an element: "))
    massive.append(new_element)

massive.sort()
counter = 0
for i in range(len(massive)-1):
    if massive[i] == massive[i+1]:
        counter += 1

print("Number of pairs: ", counter)

input()

    
