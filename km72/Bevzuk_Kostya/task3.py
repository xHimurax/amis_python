x = int(input("1st number:"))
y = int(input("2nd number:"))
z = int(input("3d number:"))
if x > y >z:
    print ("The lowest number:", z)
elif y > x > z:
    print ("The lowest number:", z)
elif x > z > y:
    print ("The lowest number:", y)
elif z > x > y:
    print ("The lowest number:", y)
elif y > z > x:
    print ("The lowest number:", x)
else:
    print ("The lowest number:", x)
   
