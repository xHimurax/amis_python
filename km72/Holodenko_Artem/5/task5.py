coordinates = [ [float(input("Enter x"+str(i)+" ")), float(input("Enter y"+str(i)+ " "))] for i in range(1,9) ]
a=True

def abs(x):
    if x<0:
        x=-x
    return x

for i in range(0, 8):
    for ii in range(0, 8):
        if coordinates[i][0]==coordinates[ii][0] or coordinates[i][1]==coordinates[ii][1] or abs(coordinates[i][0]-coordinates[ii][0])==abs(coordinates[i][0]-coordinates[ii][0]):
            a=False
if a==True:
    print("Yes")
else:
    print("No")
