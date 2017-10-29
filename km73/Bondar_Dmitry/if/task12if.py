n = int(input("Введіть кількість клітин по гризонталі:"))
m = int(input("Введіть кількість клітин по вертекалі:"))
k = int(input("Введіть потрібну кількість клітин:"))
if (n*m - k >= 0) and(( (n*m - k) % n == 0) or ( (n*m - k) % m == 0) ):
    answer = "YES"
else:
    answer = "NO"
print(answer)
input()
    
