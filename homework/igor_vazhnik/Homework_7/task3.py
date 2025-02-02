res = 'результат операции: 42'
res2 = 'результат операции: 54'
res3 = 'результат работы программы: 209'
res4 = 'результат: 2'


def calc(text):
    index = text.index(':') + 1
    print(int(text[index:]) + 10)


calc(res)
calc(res2)
calc(res3)
calc(res4)
