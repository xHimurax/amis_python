print('      Task 3 \n')
A=float(input('Enter 1-st number'))
B=float(input('Enter 2-nd number'))
C=float(input('Enter 3-rd number'))
q='My number is '
X=''
if (A<B) & (A<C):
    X= '1-st'
elif (B<A) & (B<C):
    X= '2-nd'
elif (C<B) & (C<A):
    X= '3-rd'
else:
    q='Uncorrect data'
X=q+str(X)
    
#######################################################
print(X)
d=input('Press Enter to close')
