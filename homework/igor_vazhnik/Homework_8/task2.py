# Задание 2
# Напишите функцию-генератор, которая генерирует бесконечную последовательность чисел
# фибоначчи
# Распечатайте из этого списка пятое число, двухсотое число, тысячное число,
# стотысячное число


def fibon(limit=1000000):
    a = 0
    b = 1
    count = 1
    # for _ in range(n):
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1


# print(list(fibon(1001)))

count = 1
for number in fibon(100000):
    if count == 5:
        print(number)
    elif count == 200:
        print(number)
    elif count == 1000:
        print(number)
    elif count == 100000:
        print(number)
    count += 1
