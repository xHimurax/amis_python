n=int(input("Введіть кількість хвилин після полуночі "))
while(n>1440):
    n=n-1440
hours=int(n/60)
minutes=int(n%60)
print((str)(hours),":",(str)(minutes))
input("")
