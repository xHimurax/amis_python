N = int(input('Введіть кількість хвилин, що пройшли з півночі : '))
while (N>24*60):
  N -= 24*60
hours = N//60
minutes = N%60
print(str(hours) + ':' + str(minutes))

