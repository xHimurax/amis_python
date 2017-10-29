N = int(input("студентов:"))
K = int(input("яблук:"))

appleForStudent = K // N
appleInBag = K % N
print("Сколько яблок на студента",appleForStudent)
print("Сколько яблок в ящике",appleInBag)  
