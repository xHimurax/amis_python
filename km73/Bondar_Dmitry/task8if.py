a1 = int(input("Please enter coordinate:"))
a2 = int(input("Please enter coordinate:"))
b1 = int(input("Please enter coordinate:"))
b2 = int(input("Please enter coordinate:"))
if a1 < 9 and a2 < 9 and b1 < 9 and b2 < 9:
    if abs(a1-b1) <= 1 and abs(a2-b2) <= 1:
        answer = "YES"
    else:
        answer = "NO"
else:
    answer = "Please enter the correct coordinate:"
print(answer)
input()
