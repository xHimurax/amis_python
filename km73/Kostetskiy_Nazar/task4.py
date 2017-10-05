N = int(input("Enter the number of students: "))

K = int(input("Enter the number of apples: "))

apples_per_student = K//N
apples_in_bassket = K-(K//N)*N
print("\nApples per student:",apples_per_student,"\nApples in the bassket:",apples_in_bassket)

input()
