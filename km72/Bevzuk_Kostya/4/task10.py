x = int(input("Input number1 from 1 till 8:"))
y = int(input("Input number2 from 1 till 8:"))
z = int(input("Input number3 from 1 till 8:"))
c = int(input("Input number4 from 1 till 8:"))
if x-z==2 and c-y==1:
    print ("NO")
elif z-x==2 and y-c==1:
    print ("NO")
elif x-z==2 and c-y==-1:
    print ("NO")
elif z-x==2 and y-c==-1:
    print ("NO")
elif x-z==1 and y-c==2:
    print ("NO")
elif x-z==1 and y-c==-2:
    print ("NO")
elif z-x==1 and c-y==2:
    print ("NO")
elif z-x==1 and c-y==-2:
    print ("NO")
else:
    print("Yes")
