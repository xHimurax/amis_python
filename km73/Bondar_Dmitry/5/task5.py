x=[]
y=[]

for i in range(8):
    xk = int(input("Please enter coordinate X:"))
    x.append(xk)
    yk = int(input("Please enter coordinate Y:"))
    y.append(yk)
    
answer = "No"



if answer == "No":
    for i in range(7):
        if x.count(x[i]) > 1 or y.count(y[i]) > 1:
            answer = "Yes"
            break

for i in range(7):
	if answer != "No":
		break
	k=i+1
	for k in range(k , 8):
		if ( (x[i] + y[i]) == (x[k] + y[k]) ) or ( (9 + x[i] - x[k]) == (9 +y[i] - y[k]) ):
			answer = "Yes"
			break
print(answer)
