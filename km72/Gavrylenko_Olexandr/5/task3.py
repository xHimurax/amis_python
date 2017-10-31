list = (input('Enter a list(space with a space):')).split()
final_list = []
for i in list:
    x = list.index(i)
    list.remove(i)
    if i not in list:
        final_list.append(i)
    list.insert(x, i)
print(final_list)

