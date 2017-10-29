first_number=int(input("Enter first number:"))

second_number=int(input("Enter second number:"))

third_number=int(input("Enter third number:"))

if first_number<second_number and first_number<third_number :

    answer = first_number

elif second_number<first_number and second_number>third_number :

    answer = second_number

elif third_number<first_number and third_number<second_number :

    answer = third_number

else:
  answer = "I have no answer"


print("My answer is:",answer)
input()