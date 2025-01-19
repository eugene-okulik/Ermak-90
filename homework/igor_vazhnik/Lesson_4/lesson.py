# операторы составного присваивания
# +=, -=, *=, /=, %=, **=, //=

a = 1
# a = a + 1
a += 1

print(a)

print('text' + 'text')

text = 'text'
# text = text + ' new'
text += ' new'
print(text)
symbol = '='
# symbol = symbol * 20
symbol *= 30
print(symbol)
print('Copyrights')
print(symbol)

# операторы принадлежности
# in, not in

text = 'I like ice!'
print('like' in text)
print('Like' in text)

# операторы идентичности
# is, is not

b = 2
print(id(b))
c = 2
print(id(c))
d = 257
print(id(d))
e = 257
print(id(e))
print(b is c)
print(d is e)

# способы ввода данных - клавиатура, чтение из файла, БД, API

# user_name = input('What is your name?')
# print('Hello', user_name, '!')

#ser_input = int(input('Enter number: '))
#print(type(user_input))

#print(user_input + 2)

# преобразование типов данных  str(), int(), bool(), float()

a = 1
print(type(a))
a = str(a)
print(type(a))
b = 'True'
print(type(b))
b = bool(b)
print(type(b))
print(b)
fl = '3.99'
print(type(fl))
fl = float(fl)
print(type(fl))

# типы данных в Python: Number, String, Boolean, Float, List(список), Dictionary(словарь), Tuple(кортеж), Set(множество)

# List(список)

my_list = [1, 3, 6, 7, None, 'text', False, 2.42, 'asdfg', 'last','last2']

print(type(my_list))
print(my_list)
print(my_list[2])
print(my_list[0])
print(my_list[-1])
print(my_list[-2])

my_list[-1] = 'last last'
print(my_list)

my_list2 = []
my_list3 = list()
print(my_list2)
print(my_list3)
# добавление в конец списка append()
my_list2.append(42)
my_list2.append('text')
my_list2.append('text2')
print(my_list2)
# количество элементов len()
print(len(my_list2))
# получение индекса элемента index()
print(my_list2.index('text'))
# удаление элемента из списка pop(индекс) и прихранивание
poped = my_list2.pop(0)
print(my_list2)
print(poped)

print('text' in my_list2)

# Tuple(кортеж) - скобки круглые, нельзя добавлять и изменять элементы!!!

my_tuple = (1, 3, 6, 7, None, 'text', False, 2.42, 'asdfg', 'last','last2')
print(my_tuple[2])
print(my_tuple[-1])
# my_tuple[4] = 45
# пустой кортеж
my_tuple2 = ()
my_tuple3 = tuple()
my_tuple = (1, 3, 'vcb', 'fv', 99, 'fv')
print(my_tuple)
# подсчет количества одного элемента в кортеже
print(my_tuple.count('fv'))
# получениe индекса по элементу
print(my_tuple.index(99))

llist = [56]
print(llist)
ttuple = (56,)
print(ttuple)
print(type(ttuple))

# Set(множества) фигурные скобки {}, содержить только неповторяющиеся элементы!!!, не гарантирует порядок!!!

my_set = {1, 3, 6, 7, None, 'text', False, 2.42, 'asdfg', 'last','last2'}
print(my_set)
# print(my_set[2])
my_set.add('dff')
my_set.add('text')
print(my_set)

list1 = [1, 2, 5, 6, 2, 1, 8]
print(list1)
list1 = set(list1)

print(list1)
print(type(list1))

list1 = list(list1)
print(list1)
print(type(list1))

# list1 = list(set([1, 2, 5, 6, 2, 1, 8]))

my_set2 = {} # Это словарь !!!
print(type(my_set2))
my_set3 = set() # Пустой сет можно создать только так
print(type(my_set3))

# Dictionary(словари) {'one': 'value', 'two': 'value2'}

my_dict = {'one': 'value', 'two': 'value2'}
print(my_dict)
print(my_dict['one'])
print(len(my_dict))
my_dict['one'] = 'my_value'
my_dict['three'] = 'value3'
my_dict['four'] = False
my_dict['five'] = [1, 5, 8]
my_dict['six'] = {1, 6, 9}
my_dict[2] = 'ggfgfddgf'
my_dict[False] = 'fdfgdfgd'
my_dict[1.32] = 'dfsdfs'
my_dict[(1, 2)] = 'dffsds'
my_dict[5] = {1: 2}


print(my_dict)
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())