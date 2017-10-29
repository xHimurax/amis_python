list1 = input('enter list:').split()
list2 = []
for i in range(len(list1)):
    for k in range(len(list1)):
        if (list1[i] == list1[k]) and (i != k):
            break
    else:
        list2.append(list1[i])
print(" ".join([str(i) for i in list2]))
