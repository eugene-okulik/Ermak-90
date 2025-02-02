number = 9

while True:
    user_input = input('Введите предполагаемую цифру: ')
    user_input = int(user_input)
    if user_input != number:
        print('попробуйте снова')
    else:
        print('Поздравляю! Вы угадали!')
        break
