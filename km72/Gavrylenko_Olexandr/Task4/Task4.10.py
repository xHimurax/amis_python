line_1 = int(input('Enter 1st line number:'))
column_1 = int(input('Enter 1st column number:'))
line_2 = int(input('Enter 2nd line number:'))
column_2 = int(input('Enter 2nd column number:'))
if line_1 == line_2 or column_1 == column_2 or line_1-column_1 == line_2-column_2 or line_1+column_1 == line_2+column_2:
    print('YES')
else:
    print('NO')
