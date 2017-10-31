print('Digital Clock')
minutes = int(input('Enter a number of minutes:'))
hours = minutes // 60
hours1 = hours % 24
minutes1 = minutes - hours * 60
print('Hours:'+ str(hours1) + 'minutes:'+ str(minutes1) + '.')
input()
