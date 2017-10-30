students = int(input("Кількість студентів:"))
apples = int(input("Кількість яблук:"))
ahes = 0
while apples >= students:
  apples = apples - students
  ahes += 1
print(
  "Яблук у кожного студента:"+str(ahes)+
  "\nЯблук у кошику:"+str(apples)
  )


