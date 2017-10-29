a = [int(i) for i in input().split()]
x = int(input())

result = len([i for i in a if i >= x])+1

print(result)
