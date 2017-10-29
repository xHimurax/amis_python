N=int(input("Enter N "))
K=int(input("Enter K "))
coordinates = [ [int(input("Enter li"+str(i+1)+" ")), int(input("Enter ri"+str(i+1)+ " "))] for i in range(K) ]
A=["!"]*N


for i in range(K):
    for ii in range(coordinates[i-1][0]-1,coordinates[i-1][1]):
        A[ii]="."
print(A)
