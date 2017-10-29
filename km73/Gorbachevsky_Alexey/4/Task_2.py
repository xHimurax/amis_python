x = float(input("Enter x:"))

result = "sign(x)="

if x>0:
    result += "1"
elif x==0:
    result += "0"
else:
    result += "-1"

print(result)
