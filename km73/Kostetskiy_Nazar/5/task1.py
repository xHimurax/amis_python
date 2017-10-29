a = [int(i) for i in input().split()]


x = int(input())


number = 0


while len(a)>number and x <= a[number]:


    number = number + 1


print(number + 1)