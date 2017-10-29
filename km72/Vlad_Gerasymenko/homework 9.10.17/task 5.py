while True:
    try:
        n = int(input("Введіть ЦІЛЕ число:"))
    except ValueError:
        print("Ви ввели не ціле число!")
        continue
    print("The next number for the number",n,"is",(n+1))
    print("The next previous for the number",n,"is",(n-1))
    
