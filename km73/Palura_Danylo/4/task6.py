print('      Task 6 \n')
x1 = int(input('Enter first horizontal coordinate '))
y1 = int(input('Enter first vertical coordinate  '))
x2 = int(input('Enter second horizontal coordinate '))
y2 = int(input('Enter second vertical coordinate '))
if (1<=x1<=8)&(1<=y1<=8)&(1<=x2<=8)&(1<=y2<=8):
    if ((x1 == x2) & (y1 != y2)) or ((x1 != x2) & (y1 == y2)):
        X = 'Yes'
    else:
        X = 'No'
else:
    X='Uncorrect data'
#######################################################
print(X)
d=input('Press Enter to close')