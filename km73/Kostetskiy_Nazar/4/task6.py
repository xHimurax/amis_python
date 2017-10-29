x1 = int(input("Enter the first horizontal coordinate"))
y1 = int(input("Enter the first vertical coordinate"))
x2 = int(input("Enter the second horizontal coordinate"))
y2 = int(input("Enter the second vertical coordinate"))
if x1 == x2 or y1 == y2:
	answer = "Yes"
else:
	answer = "No"
print("My answer is:",answer)
input()