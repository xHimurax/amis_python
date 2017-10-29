N = int(input('Введіть кількість яблук :'))
K = int(input('Введіть кількість студентів :'))
apple = N//K
apple_in_basket = N%K
print(str(int(apple)) + ' - кількість яблук у одного студента' '\n' + str(int(apple_in_basket)) + ' - кількість яблук у корзині' )


