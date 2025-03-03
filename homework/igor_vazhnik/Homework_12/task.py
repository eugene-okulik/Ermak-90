class Flower():
    def __init__(self, name, average_life_time, freshness, color, stemlength, price):
        self.name = name
        self.average_life_time = average_life_time
        self.freshness = freshness
        self.color = color
        self.stemlength = stemlength
        self.price = price

class TypeFlower(Flower):
    def __init__(self, name, average_life_time, freshness, color, stemlength, price, special):
        super().__init__(name, average_life_time, freshness, color, stemlength, price)
        self.special = special


class Bouquet():

    flowers = []

    def wilting_time(self):
        life_time_sum = 0
        for flower in self.flowers:
            life_time_sum += flower.average_life_time
        return life_time_sum / len(self.flowers)

    def find_average_life_time(self):
        print(f'Цветы по среднему времени жизни более 5 дней:')
        for flower in self.flowers:
            if flower.average_life_time > 5:
                print(f'{flower.name} {flower.average_life_time}')


    def gen_sum(self):
        sum = 0
        for flower in self.flowers:
            sum += flower.price
        return sum


flower = TypeFlower('Розы', 5, 10, 'Красные', 50, 40,
                    'много шипов')
flower2 = TypeFlower('Розы', 6, 10, 'Розовые', 60, 35,
                     'много шипов')
flower3 = TypeFlower('Тюльпаны', 7, 8, 'Белые', 65, 30,
                     'нет особеностей')
bouquet = Bouquet()
bouquet.flowers.append(flower)
bouquet.flowers.append(flower2)
bouquet.flowers.append(flower3)

print(f'Среднее время увядания букета', bouquet.wilting_time())
bouquet.find_average_life_time()
print(f'Общая сумма букетов', bouquet.gen_sum())
