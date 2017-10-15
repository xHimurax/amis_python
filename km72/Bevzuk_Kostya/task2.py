try:
    x = float(input("Enter number:"))
except:
    ValueError
    print("Incorrect")
if x > 0:
    print ("+")
if x < 0:
    print ("-")
if x == 0:
    print (")")
