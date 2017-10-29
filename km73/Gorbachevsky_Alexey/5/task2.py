a = [int(i) for i in input().split()]

new_a = [(i,j) for i in a for j in a if i==j]
result = (len(new_a)-len(a))//2

print(result)
