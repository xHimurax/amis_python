a = int(input("Введіть перше число:"))
b = int(input("Введіть друге число:"))
c = int(input("Введіть третє число:"))
if a <= b and a <= c:
  answer = a
if b <= c and b <= a:
  answer = b
if c <= a and c <= b:
  answer = c
print(answer)
input()
