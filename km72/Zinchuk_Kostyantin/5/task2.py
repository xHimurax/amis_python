_list=(input("enter list ")).split()
_counter=0
for i in _list:
    for j in _list:
        if i==j:
            _counter=_counter+1        
    _counter=_counter-1
print(_counter/2)
