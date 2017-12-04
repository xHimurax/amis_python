x = int(input("Введiть кiлькiсть елементiв списку - "))
list_numbers = []

'''
Користувач вводить кiлькiсть елементiв списку, та створюеться порожнiй список list_numbers
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
да дiе допоки його довжина менше нiж кiлькiсть елементiв
'''

def minimum(list_numbers):
    if len(list_numbers) == 0:
        return
    if len(list_numbers) == 1:
        return list_numbers[0]
    min_elem = minimum(list_numbers[1:])
    if min_elem < list_numbers[0]:
        return min_elem
    else:
        return list_numbers[0]
'''
Створюеться рекурсивна функцiя minimum, що повертае нiчого, якщо довжина list_numbers = 0, перший (та единий)
елемент списку, коли довжина list_numbers = 1. Якщо бiльше одного, то пробiгае по всiм елементам, шляхом
зменшення списку на елемент при кожному виклику функцii, та порiвнюе елементи, i виводить найменший.
'''

print("Мiнiмальний елемент списку -",minimum(list_numbers))
