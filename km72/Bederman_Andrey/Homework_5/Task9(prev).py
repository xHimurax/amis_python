list = [int(i) for i in input("enter list:").split()]
for i in range(1,len(list),2):
	a = list[i]
	list[i] = list[i-1]
	list[i-1] = a
for i in list:
	print(i, end=' ')
input("\n\nPress Enter to exit the program.")
