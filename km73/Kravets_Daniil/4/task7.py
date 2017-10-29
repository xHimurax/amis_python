print("Enter coordinate of first square")
x0=int(input())
y0=int(input())
print("Enter coordinate of second square")
x1=int(input())
y1=int(input())
if (1<=x0<=8) and (1<=y0<=8) and (1<=x1<=8) and (1<=y1<=8):
    if ((x0%2==1) and (y0%2==1) and (x1%2==1) and (y1%2==1)) or (((x0%2==0) or (y0%2==0)) and ((x1%2==0) or (y1%2==2))):
        answer="YES"
    else:
        answer="NO"
else:
    answer="YOU ARE AN IDIOT"
print(answer)

