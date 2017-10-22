list = input("enter list:").split()
a = 0
for i in range(1, len(list)-1):
    if int(list[i-1]) < int(list[i]) and int(list[i]) > int(list[i+1]):
        a += 1
print(a)
input("\n\nPress Enter to exit the program.")
