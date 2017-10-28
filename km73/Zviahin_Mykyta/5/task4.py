massive = []
N = int(input("Number of skittles: "))
cointer = 0
for i in range(N):
    skittle = 'I'
    massive.append(skittle)
K = int(input("Number of shots: "))
for j in range(K):
    li = int(input("Enter the lowest number of knocked-down skittles: "))
    ri = int(input("Enter the highest number of knocked-down skittles: "))
    if ri >= li:
        for i in range(li,ri+1):
            massive[i-1] = '.'
    

for i in range(N):
    print(massive[i], end = ' ')

input()
        
             



