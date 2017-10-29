list=input("enter list:").split()
for i in range(len(list)):
    if i % 2 == 0:
        print(list[i], end=" ")
input("\n\nPress Enter to exit the program.")
