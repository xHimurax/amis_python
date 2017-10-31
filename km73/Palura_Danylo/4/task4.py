print('      Task 4 \n')
A=int(input('Enter year'))

X='Uncorrect data'
if (A>=0) & ((A%4) == 0):
    X= 'LEAP'
elif (A>=0) & ((A%4) != 0):
    X= 'COMMON'
#######################################################
print(X)
d=input('Press Enter to close')
