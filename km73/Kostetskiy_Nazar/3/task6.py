import math
group_a = int(input('Enter the number of students A: '))
group_b = int(input('Enter the number of students B: '))
group_c = int(input('Enter the number of students C: '))
tables = math.ceil((group_a + group_b + group_c)/2)
print("\nYou have to buy",tables,"tables")
input()