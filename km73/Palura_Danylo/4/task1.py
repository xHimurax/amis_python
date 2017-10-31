print('      Task 1 \n')
A=float(input('Enter 1-st number'))
B=float(input('Enter 2-nd number'))
if A<B:
    X=A
    X='My answer is '+str(X)
elif B<A:
    X=B
    X='My answer is '+str(X)
else:
    X='Uncorrect data'
#######################################################
print(X)
d=input('Press Enter to close')
