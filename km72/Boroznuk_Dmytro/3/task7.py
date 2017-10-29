import time
N=int(input("Введите количество минут:"))
hours=(N%1440)//60
"""(N%1440) к-сть хвилин,коли відкидаються завершені дні
(N%1440)//60 к-сть завершених годин"""
minutes=(N%60)
print(str(hours)+":" +str(minutes))
time.sleep(3)
