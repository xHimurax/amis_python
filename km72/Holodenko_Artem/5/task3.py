S=input("Enter string")
n=len(S)
boolean=[True]*n

for i in range(n):
    for ii in range(n):
        if S[i]==S[ii]:
            if i==ii:
                continue
            else:
                boolean[i]=False
                boolean[i]=False
for i in range(len(boolean)):
    if boolean[i]==True:
        print(S[i])
