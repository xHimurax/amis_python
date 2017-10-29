line = input("Enter height of each pupil:").split()
for i in range(len(line)):
    line[i] = int(line[i])
Petya = int(input("Petya's height:"))
line.append((Petya))
line.sort()
line = line[::-1]

same_h = line.count(Petya)
place = line.index(Petya)+same_h
print("Petya should stay:", place)
print(input("Click on \"Enter\" to close program"))