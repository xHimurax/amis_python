n = int(input("Enter number of cells in height: "))
m = int(input("Enter number of cells in width: "))
k = int(input("Enter number of cells you need to cut off: "))

if (((k % n) == 0) or ((k % m) == 0)) & ((m * n) >= k):
    print("You can cut the piece off in one step")
else:
    print("You can't cut the piece off in one step.")

input()
