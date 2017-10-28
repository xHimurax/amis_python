x1 = int(input('First coordinate : '))
y1 = int(input('Second coordinate : '))
x2 = int(input('Third coordinate : '))
y2 = int(input('Fourth coordinate : '))

if (0 < x1 < 9) & (0 < y1 < 9) & (0 < x2 < 9) & (0< y2 < 9) :
    if (x1+y1)%2 == (x2+y2)%2 :
        answer = 'Yes'
    else :
        answer = 'No'
else :
    answer = 'No'
print(answer)