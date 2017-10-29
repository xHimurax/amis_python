fnum=int(input("Enter first number:"))
snum=int(input("Enter second number:"))
thnum=int(input("Enter third number:"))
if fnum<=snum and fnum<=thnum:
    print("min number=", fnum)
elif snum<=fnum and snum<=thnum:
    print("min number=", snum)
else:
    print("min number=", thnum)
input("\n\nPress Enter to exit the program.")
