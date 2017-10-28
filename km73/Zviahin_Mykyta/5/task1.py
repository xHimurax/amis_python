form = []
n = int(input("Enter the number of students: "))
for i in range(n):
    
    new_element = int(input("Enter the height of a student: "))
    if new_element > 200:
        print("This height is too much for a student:)")
    elif new_element < 0:
        print("Enter the positive number")
    else:
        form.append(new_element)

x = int(input("Enter the Petyas height: "))

pos = 0

while pos < len(form) and form[pos] >= x :
    pos += 1

print(pos + 1)

input()

