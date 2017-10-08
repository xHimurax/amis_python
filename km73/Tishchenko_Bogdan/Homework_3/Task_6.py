import math

print("Enter the number of students in the first group")
group1 = int(input())
print("Now in the second ")
group2 = int(input())
print("And in the third")
group3 = int(input())

tables = math.ceil(group1/2) + math.ceil(group2/2) + math.ceil(group3/2)
print("You need", tables)
