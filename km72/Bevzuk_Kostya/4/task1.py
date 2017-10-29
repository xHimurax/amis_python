try:
    x = int(input("Input first number:"))
except:
    ValueError
    print("Incorect")
try:
    y = int(input("Input second number:"))
except:
    ValueError
    print("Incorect")    
if x > y :
    print("The lowest:", y)
else:
    print("The loswest:", x)
