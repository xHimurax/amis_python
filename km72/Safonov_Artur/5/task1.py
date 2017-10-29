
list = input("Enter growths using a 'space' button: ").split()
peter_gr = float(input("Enter the growth of Peter: "))

num = 1
for i in list:
    if float(i) >= peter_gr:
        num += 1

print("Peter`s number = " + str(num))
