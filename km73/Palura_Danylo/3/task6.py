print("                         Задача №6")
print("\nВсi вiд'ємнi числа будуть взятi по модулю")
A=abs(int(input("\nСкiльки учнiв у першiй групi?")))
if A>=200000:
    print("Забагато учнiв")
else:
    B=abs(int(input("Скiльки учнiв у другiй групi?")))
    if B>=200000:
        print("Забагато учнiв")
    else:
        C=abs(int(input("Скiльки учнiв у третiй групi?")))
        if C>=200000:
            print("Забагато учнiв")
        else:
#getting variables
#MAIN CODE
            X=(A+1)//2+(B+1)//2+(C+1)//2
            X="Потрiбно парт: "+str(X)
#outputting the result
            print(X)        
d=input("Натиснiть Enter для завершення програми")
