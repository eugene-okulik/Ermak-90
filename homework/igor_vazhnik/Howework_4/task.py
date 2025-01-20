my_dict = {'tuple': '', 'list': '', 'dict': '', 'set': ''}
my_dict['tuple'] = (1, 'two', 3, 'four', 5)
my_dict['list'] = ['one', 2, 'three', 4, 'five']
my_dict['dict'] = {'jan': '0', 'feb': '1', 'mar': '3', 'apr': '4', 'may': '5'}
my_dict['set'] = {1, 'tru', 2.5, 'qwer', 34}
# Последний элемент кортежа
print(my_dict['tuple'][-1])
# Добавление элемента в конец списка
my_dict['list'].append('last')
# Удаление второго элемента списка
my_dict['list'].pop(1)
# Добавление элемента с ключом ('i am a tuple'),
my_dict['dict'][('i am a tuple',)] = 'i am a tuple!'
# Удаление элемента
my_dict['dict'].pop('jan')
# Добавление нового элемента в множество
my_dict['set'].add('zxcv')
# Удаление элемента из множества
my_dict['set'].pop()
print(my_dict)
