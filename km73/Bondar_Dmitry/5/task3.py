x = input("Введіть список: ").split()
b=[]
for i in range(len(x)):
	if x.count(x[i]) == 1:
		b.append(x[i])
print(b)
