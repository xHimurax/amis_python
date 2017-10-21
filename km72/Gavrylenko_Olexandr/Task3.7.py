import time
N = int(input('Enter number of minutes:'))
while N > 1440:
    N = N-1440
hours = N//60
minutes = N%60
print('Hours:', hours,'\nMinutes:', minutes)
time.sleep(5)
