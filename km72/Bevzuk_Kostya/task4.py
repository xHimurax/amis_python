x = int(input("Input year:"))
y = x//400
z = x//4
if x == y*400:
    print("LEAP")
elif x == z*4 and x%100 :
    print("LEAP")
else:
    print("COMMON")
