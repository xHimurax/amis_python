list = input("enter list:").split()
index = 0
for i in range(0, len(list)-1):
    if int(list[i]) != int(list[i+1]):
        index +=1
print(index+1)
input("\n\nPress Enter to exit the program.")
