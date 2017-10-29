list = input("enter list:").split()
height = int(input("enter height:"))
height_ind = 0
for i in range(0, len(list)):
    a = int(list[i])
    if a >= height:
        height_ind = i + 1
print(height_ind + 1)
input("\n\nPress Enter to exit the program.")
