result = 'результат операции: 42'
result2 = 'результат операции: 514'
result3 = 'результат работы программы: 9'
print(result)
index = result.index(':') + 1
res = int(result[index:])
print(res + 10)
print(result2)
index = result2.index(':') + 1
res = int(result2[index:])
print(res + 10)
print(result3)
index = result3.index(':') + 1
res = int(result3[index:])
print(res + 10)
