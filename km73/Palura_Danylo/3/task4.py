print("                         Задача №4")
#getting variables
print("Всi вiд'ємнi числа будуть взятi по модулю")
A = int(input("Скiльки студентiв?"))
#MAIN CODE
if A==0:
    print("Нiкому отримувати яблука")
elif A>=8000000000:
    print("Де ви бачили стiльки людей взагалi?")
elif A>=3800000000:
    print("Отже на планетi бiльше половини людей - студенти?")
else:
    B = int(input("Скiльки яблук?"))
    if A>0:
        A=A
    else: A=-A
    if B>=0:
        B=B
    else: B=-B
    X=B//A
    Y=B%A
#########################
    if (X+10-1)%10==0:
        Apple1="яблуко"
    elif (X+10-2)%10==0:
        Apple1="яблукa"
    elif (X+10-3)%10==0:
        Apple1="яблукa"
    elif (X+10-3)%10==0:
        Apple1="яблукa"
    else:
        Apple1="яблук"
#########################
    if (Y+10-1)%10==0:
        Apple2="яблуко"
    elif (Y+10-2)%10==0:
        Apple2="яблукa"
    elif (Y+10-3)%10==0:
        Apple2="яблукa"
    elif (Y+10-3)%10==0:
        Apple2="яблукa"
    else:
        Apple2="яблук"
########################
#outputting the result
    print("у студентiв по", X, Apple1, "\n"+"В кошику", Y, Apple2)
d=input("\nНатиснiть Enter для завершення програми")
