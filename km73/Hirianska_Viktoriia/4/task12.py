n=int(input("Enter the number of columns: "))
m=int(input("Enter the number of rows: "))
k=int(input("Enter the number of cells that you want to receive: "))
if ((k%n)==0 or (k%m)==0) and ((m*n)>=k):
    print("YES")
else:
    print("NO")
input()
