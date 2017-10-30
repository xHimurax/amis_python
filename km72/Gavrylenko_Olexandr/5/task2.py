list = (input('Enter list of numbers(space with a space):')).split()
repeats = []
for i in list:
    list.remove(i)
    if i in list:
        repeats.append(i)
    print(list)
print(len(repeats))
            
        
    
