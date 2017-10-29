print("This program calculates how many hours and minutes passed from 00:00")
N=int(input("Enter the number of minutes:"))
print("Time:", (N%1440)//60, ":", N%60)
input("\n\nPress Enter to exit the program.")
