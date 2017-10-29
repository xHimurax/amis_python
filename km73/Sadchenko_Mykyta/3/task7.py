allMins = int(input("Enter number of minutes: "))
hours = (allMins//60)%24
mins = allMins%60
print("Real time - ",hours,":",mins)
