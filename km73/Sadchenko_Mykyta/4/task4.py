while True:
    year = int(input("Enter value of years: "))

    if year > 0:
        if (year%400 == 0) | ((year%4 == 0)&(year%100 != 0)):
            print("\nLEAP")
        else:
            print("\nCOMMON")
        break
    else:
        print("\nNeed a positive number")
        continue
    
