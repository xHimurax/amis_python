minutes = int(input("Vvedit' kil'kist' khvylyn: "))


hours = minutes // 60
minutes = minutes % 60

while hours >= 24:
    hours = hours - 24

print("Chas: ", hours, ':', minutes)

input()

