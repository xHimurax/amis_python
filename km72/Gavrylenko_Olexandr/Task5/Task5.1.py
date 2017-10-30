group = (input('Enter growth of students(space with a space):')).split()
x = input('Enter Petya growth:')
group.append(x)
print(group)
students = sorted(group)
line = students[::-1]
print(line)
line_index = line.index(x)
for i in line:
    if i == x:
        line_index = line_index + 1
print(line_index)


