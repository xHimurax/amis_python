print("                         Задача №7")
print("\nВiд'ємне число буде взяте по модулю")
N=abs(int(input("\nСкiльки годин пройлшло з пiвночi?")))
#getting variables
#MAIN CODE
H=(N%1440)//60
M=N%60
if H<10:
    H="0"+str(H)
else:
    H=str(H)
if M<10:
    M="0"+str(M)
else:
    M=str(M)
X="\nГодинник показує "+H+":"+M+"\n"
#outputting the result
print(X)        
d=input("Натиснiть Enter для завершення програми")
