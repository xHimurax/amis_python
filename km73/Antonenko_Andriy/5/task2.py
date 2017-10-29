a = input('Введіть елементи списку : ').split( )
s = 0
for element in a:
    two = a.count(element)
    if two%2==1:
      cr = two//2
      s = s+cr
    else:
        s = s+(two//2)
print('Кількість однакових елементів: ' + str(s))
