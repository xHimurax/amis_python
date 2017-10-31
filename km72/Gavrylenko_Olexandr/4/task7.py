line_1 = int(input('Enter 1st line number:'))
column_1 = int(input('Enter 1st column number:'))
line_2 = int(input('Enter 2nd line number:'))
column_2 = int(input('Enter 2nd column number:'))
if (line_1 + column_1)%2 == 0 and (line_2 + column_2)%2 == 0 or (line_1 + column_1)%2 != 0 and (line_2 + column_2)%2 != 0:
    print('YES')
else:
    print('NO')
