import random

salary = 0
bonus = True

salary = int(input('Your salary: '))
bonus = bool(random.randint(0, 1))

if bonus == True:
    print(f'{salary}, {bonus} - \'${salary + (int)(salary * random.random())}\'')
else:
    print(f'{salary}, {bonus} - \'${salary}\'')
