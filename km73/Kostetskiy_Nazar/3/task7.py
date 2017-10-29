N = int(input("How many minutes passed?\n"))
days = (N/60)//24
hour = int(N//60 - days*24)
N = N%60
print("\nYour time is",hour,":",N)
input()