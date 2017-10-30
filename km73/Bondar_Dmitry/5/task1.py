hight = input("Введіть зріст людей в строю: ").split()
PetyaHight=int(input("Введіть зріст Петі: "))
answer = 1
for i in range(len(hight)):
    if int(hight[i]) >= PetyaHight:
       answer +=1 
        
    
print(answer)

