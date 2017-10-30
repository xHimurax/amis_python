N = int(input("введите количество минут - "))
K = 0
while N >= 60:
    N = N - 60
    K = K + 1
while K >= 24:
    K = K - 24
print("кол-во часов - ",K,"кол-во минут - ",N)
input()
