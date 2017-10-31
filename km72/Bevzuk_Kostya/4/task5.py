x = int(input("1st number:"))
y = int(input("2nd number:"))
z = int(input("3d number:"))
if x==y==z:
    print("Answer:3")
elif x==y:
    print("Answer:2")
elif x==z:
    print ("Answer:2")
elif y==z:
    print("Answer:2")
else:
    print("Answer:0")
