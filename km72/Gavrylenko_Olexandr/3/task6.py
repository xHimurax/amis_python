import time
stud1 = int(input('Enter number of students in 1st class:'))
stud2 = int(input('Enter number of students in 2nd class:'))
stud3 = int(input('Enter number of students in 3rd class:'))
x = (stud1 + stud2 + stud3)%2
print('Minimal number of tables needed:', (stud1 + stud2 + stud3)//2 + x)
time.sleep(3)
