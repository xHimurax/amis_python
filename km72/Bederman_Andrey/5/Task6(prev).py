list = input("enter list:").split()
number = int(list[0])
index = 0
for i in range(1, len(list)):
    a = int(list[i])
    if a > number:
        number = a
        index = i
print(number, index)
input("\n\nPress Enter to exit the program.")
