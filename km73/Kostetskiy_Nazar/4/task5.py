first_number=int(input("Enter first number:"))

second_number=int(input("Enter second number:"))

third_number=int(input("Enter third number:"))

if first_number == second_number == third_number:
  
    answer = 3

elif first_number == second_number or first_number == third_number:
 
    answer = 2

elif second_number == third_number:

    answer = 2

else:
  answer = 0

print("My answer is:",answer)
input()