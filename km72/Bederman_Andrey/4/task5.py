a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=int(input("Enter 3d number:"))
if a==b==c:
    print("3")
elif a==b or a==c or b==c:
    print("2")
else:
    print("0")
input("\n\nPress Enter to exit the program.")
