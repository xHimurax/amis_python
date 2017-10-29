class1 = int(input("Vvedit' kil'kist' uchniv pershoyi grupy: "))
class2 = int(input("Vvedit' kil'kist uchniv vtoroyi grupy: "))
class3 = int(input("Vvedit' kil'kist' uchniv tretyoyi grupy: "))

allstudents = class1 + class2 + class3

integerpart = allstudents // 2
remainder = allstudents % 2

tables = integerpart + remainder

print("Minimal'na kil'kist' stoliv: ", tables)

input()
