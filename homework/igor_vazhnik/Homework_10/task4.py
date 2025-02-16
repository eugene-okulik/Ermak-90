PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

print(PRICE_LIST)

# res_dict = dict((a.strip(), int(b.strip()))
#            for a, b in (element.split()
#               for element in PRICE_LIST.split('\n')))

res_dict = dict((a, int(b.strip('р')))
    for a, b in (element.split()
        for element in PRICE_LIST.split('\n')))

print(res_dict)
# {'тетрадь': 50, 'книга': 200, 'ручка': 100, 'карандаш': 70, 'альбом': 120, 'пенал': 300, 'рюкзак': 500}
