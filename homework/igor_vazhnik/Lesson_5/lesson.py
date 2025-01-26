# Распаковка

my_list = [1, 3]
my_tuple = (2, 6, 9)

# a = my_list[0]
# b = my_list[1]
# c = my_tuple[0]
# d = my_tuple[1]
# e = my_tuple[2]
a, b = my_list
#a = my_list
c, d, e = my_tuple
# print(c, d, e)
# print(a)
print(a, b, c, d, e)

# Срез - получение части списка [от(можно не писать):до не включая]

lll = [1, 3, 5, 2, 5, 7, 1, 3]
print(lll)
print(lll[1:4])
print(lll[:4])
print(lll[1:])
# шаг среза
print(lll[1::2])
# в обратном порядке
print(lll[::-1])
print(lll[::-2])
print(lll[-2:-6:-1])

# Методы строк
text = 'my long long string'
print(text[3])
print(len(text))
print(text.index('long'))
print('ma' in text)
print(text.count('n'))
print(text.count('long'))
print(text.find('lonl'))
print(text[:7])
print(text.startswith("my"))
print(text.endswith("string"))

txt = "ThIs tExt wiTh meSsEd uP CaPITalIZatiOn!"
print(txt)
# Делает первую букву предложения заглавной, остальные в нижнем регистре
print(txt.capitalize())
# Делает каждую первую букву заглавной
print(txt.title())
# Делает все буквы большими
print(txt.upper())
# Делает все буквы маленькими
print(txt.lower())
text = 'mY lOng loNg stRing'
print(text)
string_index = text.lower().index('string')
print(text[:string_index].lower() + text[string_index:].upper())

msg = 'Hello world!'
msg2 = msg.replace('world', 'universe')
print(msg)
print(msg2)

data = '12,3'
data = data.replace(',','.')
print(data)

txt = ' admin '
print(txt)
# txt = txt.replace(' ', '')
# txt = txt.strip()
# txt = txt.lstrip()
txt = txt.rstrip()
print(txt)
text = '"name"'
print(text)
text = text.strip('"')
print(text)

# Строка <-> список
# Строка -> список

my_string = 'some little text'
my_string2 = 'some,little,text'
print(my_string)
print(my_string2)
list_from_text = my_string.split()
print(list_from_text)
list_from_text2 = my_string2.split(',')
print(list_from_text2)

# Список -> строка
languages = ['Python', 'Java', 'Ruby']
print(languages)
# languages = ', '.join(languages)
print(languages)
print('Student knows these languages:', ', '.join(languages))

# Форматирование строки
a = 'one'
b = 'two'
print('First word is', a, ',second word is', b)

my_text = 'First word is ' + a + ', second word is ' + b
print(my_text)

# устаревший метод
my_text = 'First word is %s, second word is %s'
print(my_text % (a, b))

# более новый стринг формат
my_text = 'First word is {}, second word is {}'
print(my_text.format(a, b))

my_text = 'First word is {1}, second word is {0}'
print(my_text.format(a, b))

# f-string
my_text = f'First word is {a}, second word is {b}'
print(my_text)

template = 'Hello, {0}!'
username = input('What is your name?')
print(f'Hello, {username}!')
print(template.format(username))
