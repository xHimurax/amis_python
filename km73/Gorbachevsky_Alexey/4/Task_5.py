a = int(input("Enter first_number: "))
b = int(input("Enter second_number: "))
c = int(input("Enter third_number: "))

a_b = a - b
b_c = b - c
a_c = a - c

result = 0
if not a_b:
    result += 1
if not a_c:
    result += 1
if not b_c:
    result += 1
if result == 1:
    result += 1

print(result)
