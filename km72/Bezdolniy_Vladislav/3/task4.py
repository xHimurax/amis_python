import time
print("             Добрый день!")
N = float(input('Введите количество студентов ='))
K = float(input('Введите количество яблок ='))
x = K // N
y = K - N*(K // N)
print("У студентов по", x, "яблок")
print("В корзине", y, "яблок")
time.sleep(3)
