list = input("Enter the list of numbers using a 'space' button: ").split()

num = 0
for i in range(len(list)):
    for j in list[0:i]+list[i+1:]:
        if list[i] == j:
            num += 1

num = num//2

print("Number of pairs of elements equal to each other: " + str(num))

