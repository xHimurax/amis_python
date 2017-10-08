import time
students=int(input("Введите число студентов:"))
apples=int(input("Введите число яблок:"))
print("Every student will have "+str(apples//students)+" apples")#Сколько будет яблок у каждого студента
print("In basket they have "+str(apples%students)+" apples")#Сколько яблок останется в ящике
time.sleep(3)
