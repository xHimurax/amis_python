x = int(input("Введiть кiлькiсть елементiв списку - "))
list_numbers = []

'''
'Користувач вводить кiлькiсть елементiв списку, та створюеться порожнiй список list_numbers'
'''

def form_list(x):
    global list_numbers
    if len(list_numbers) < x:
        list_numbers.append(int(input("Введiть число - ")))
        form_list(x)
    else:
        return list_numbers

form_list(x)

'''
Створюеться, та, в подальшому, викликаеться функцiя form_list, що додае введенi користувачем числа до list_numbers,
да дiе допоки його довжина менше нiж кiлькiсть елементiв'
'''

def reverse(list_numbers):
    if len(list_numbers) < 2:
        return list_numbers
    else:
        middle = len(list_numbers)//2
        return (reverse(list_numbers[middle:]) + reverse(list_numbers[:middle]))

'''
Створюеться функцiя, що повертае список list_numbers, якщо його довжина меньша за 2, 
'''

print(reverse(list_numbers))
