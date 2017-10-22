list = input("enter list:").split()
for i in range(len(list)-1):
     a = int(list[i])
     i += 1
     b = int(list[i])
     if b > a:
         a = b
         print(b, end=" ")
input("\n\nPress Enter to exit the program.")
