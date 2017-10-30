isError=True
while isError:
    _string=input("enter string: ")
    _list=_string.split()
    for element in _list:
        if int(element)>200:
            isError=True
            break
        elif int(element)<130:
            isError=True
            break
        elif int(element)>130 and int(element)<=200:
            isError=False
            break
    if isError:
        print("Not correct data")
        continue
    else:
        break
isError=True
_heightPetya=0
while isError:
    _heightPetya=int(input("enter height: "))
    if _heightPetya>200 and _heightPetya<130:
        isError=True
        break
    else:
        isError=False
        break
    if isError:
        print("Not correct data")
        continue
    else:
        break

_PetyaPosition=0
for i in range(0,len(_list)):
    index=int(_list[i])
    if index>_heightPetya:
        _PetyaPosition=i+1
print(_PetyaPosition+1)

    
        

     
