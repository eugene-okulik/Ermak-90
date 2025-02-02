res = 'результат операции: 42'
res2 = 'результат операции: 54'
res3 = 'результат работы программы: 209'
res4 = 'результат: 2'

def sum(text):
    index = text.index(':') + 1
    print(int(text[index:]) + 10)

sum(res)
sum(res2)
sum(res3)
sum(res4)
