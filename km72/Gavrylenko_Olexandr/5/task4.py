N = int(input('Enter number of skittles:'))
line = list('|'*N)
x = '.'
K = int(input('Enter number of shots:'))
for i in range(K):
    li = int(input('Enter li:'))
    ri = int(input('Enter ri:'))
for element in line:
    print(line.index(element))
    if li<=line.index(element)+1<=ri:
        line.insert(line.index(element), x)
        line.remove(element)
print(line)
