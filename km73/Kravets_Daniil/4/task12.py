print ("Enter size of chocolade n*m")
n=int(input())
m=int(input())
print ("Enter number of pieses")
k=int(input())
if (k%n==0) or (k%m==0):
    answer="YES"
else:
    answer="NO"
print(answer)
