print('      Task 9 \n')
x1 = int(input('Enter first horizontal coordinate '))
y1 = int(input('Enter first vertical coordinate  '))
x2 = int(input('Enter second horizontal coordinate '))
y2 = int(input('Enter second vertical coordinate '))
if (1<=x1<=8)&(1<=y1<=8)&(1<=x2<=8)&(1<=y2<=8):
    if (abs(x1-x2) == abs(y1-y2)) & ((x1-x2) != 0):
        X = 'Yes'
    else:
        X = 'No'
else:
    X='Uncorrect data'
#######################################################
print(X)
d=input('Press Enter to close')
