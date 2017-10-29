N = input("Введіть, будь ласка, кількість хвилин >> ")
N = int(N)
hours = N//60
minutes = N%60
print("Время:",(hours%24),":",(minutes))