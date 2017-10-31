N = int(input("Count of min:"))
K = N//1440
R = N-K*1440
Hour = R//60
Minut = R-Hour*60
print('Hours', Hour, 'Minutes', Minut)
