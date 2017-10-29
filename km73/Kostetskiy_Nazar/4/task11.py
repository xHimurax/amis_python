x1 = int(input("Enter the first horizontal coordinate "))

y1 = int(input("Enter the first vertical coordinate "))

x2 = int(input("Enter the second horizontal coordinate "))

y2 = int(input("Enter the second vertical coordinate "))

if x2 == x1 + 2 and y2 == y1 + 1:

    answer = "Yes"

elif x2 == x1 + 2 and y2 == y1 - 1:

    answer = "Yes"

elif x2 == x1 - 2 and y2 == y1 + 1:

    answer = "Yes"

elif x2 == x1 - 2 and y2 == y1 - 1:

    answer == "Yes"

elif x2 == x1 + 1 and y2 == y1 + 2:

    answer = "Yes"

elif x2 == x1 - 1 and y2 == y1 + 2:

    answer = "Yes"

elif x2 == x1 - 1 and y2 == y1 - 2:

    answer = "Yes"

elif x2 == x1 + 1 and y2 == y1 - 2:

    answer = "Yes"

else:

    answer = "No"

print("My answer is:",answer)

input()