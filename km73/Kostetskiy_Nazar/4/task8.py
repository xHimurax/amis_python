x1 = int(input("Enter the first horizontal coordinate "))

y1 = int(input("Enter the first vertical coordinate "))

x2 = int(input("Enter the second horizontal coordinate "))

y2 = int(input("Enter the second vertical coordinate "))

if (x2 - x1 > 1) and (-1 < x2 - x1):

    answer = "No"

elif (y2 - y1 > 1) and (-1 < y2 - y1):

    answer = "No"

else:
    answer ="Yes"

print("My answer is:",answer)

input()