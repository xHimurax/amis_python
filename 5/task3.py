_list=(input("enter list : ")).split()
_list2=[]
for i in range(len(_list)):
    for j in range(len(_list)):
        if (_list[i] == _list[j]) and (i != j):
            break
    else:
        _list2.append(_list[i])
print(' '.join([str(i) for i in _list2]))
