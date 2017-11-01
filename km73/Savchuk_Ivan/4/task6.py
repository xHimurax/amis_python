n=int(input("hello, please enter the number of students  in first group:",))
g=int(input('Please, enter the number of students in second group:',))
z=int(input('Please, enter the number of students in third group:',))
d1=(n+g+z)//2
d2=(n+g+z)%2
print('the number of needed desks:', d1+d2)