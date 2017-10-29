string = input().split()
X = int(input())
heigh = 0
for element in range(0, len(string)):
    a = int(string[element])
    if a >= X:
        heigh = element+1
print(heigh+1)
