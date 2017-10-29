first_number=int(input("Enter first number:"))
second_number=int(input("Enter second number:"))

if first_number< second_number:
    answer = first_number
elif first_number > second_number:
    answer = second_number
else:
    answer = "Enter different numbers, please"

print("\n"+"My answer is:",answer)
input()