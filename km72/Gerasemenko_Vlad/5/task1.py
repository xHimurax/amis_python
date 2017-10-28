X = int(input("Введіть зріст Петі:"))
students = input("Введіть зрости учнів").split()
index = 0
for i in range(len(students)):
    n = int(students[i])
    if n>=X:
        index = i+1
        print(index+1)
