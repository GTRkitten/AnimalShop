class Animal:
    def __init__(self, name:str, price):
        self.name = name
        self.price = price

    def sound(self):
        return f'Звук'

class Dog(Animal):
    def sound(self):
        super().sound()
        return f'Гав!'

class Cat(Animal):
    def sound(self):
        super().sound()
        return f'Мяууу!'

class Bird(Animal):
    def sound(self):
        super().sound()
        return f'Чирик-чирик!'


class Shop:
    def __init__(self, name:str,
                 budget:int,
                 animals:list):
        self.name = name
        self.animals = animals
        self.budget = budget

    def __str__(self):
        return f'Бюджет магазина {self.name}: {self.budget}'

    def buy_animal(self, animal:Animal):
        if self.budget >= animal.price:
            self.budget -= animal.price
            self.animals.append(animal)
            print(animal.sound())
        else:
            print(f'На покупку {animal.name} у {self.name} недостаточно денюжек :(')

    def sell_animal(self, animal):
        if animal in self.animals:
            self.budget += animal.price
            self.animals.remove(animal)
            print(animal.sound())
        else:
            print(f'{animal.__class__.__name__} по имени {animal.name} в {self.name} нет')


###########GETTING NAMES
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup as soup


url = 'https://zoo-perm.ru/novosti/krasivye-imena-dlya-koshek-putevoditel-po-vyboru-idealnogo-imeni-dlya-vashego-pushistogo-druga/'
headers = {'User-Agent': UserAgent().random}
html = requests.get(url, headers=headers)
names = soup(html.content, 'html.parser')
c_names = names.select('blockquote')[1].text.strip('').split()
cat_names = []
for name in c_names:
    cat_names.append(name[0:-1])
# print(cat_names)



url = 'https://www.purinaone.ru/dog/articles/new-owner-tips/klichki-dlya-sobak-malchikov'
headers = {'User-Agent': UserAgent().random}
html = requests.get(url, headers=headers)
names = soup(html.content, 'html.parser').select('table')[1].select('p')
dog_names = []
for name in names:
    dog_names.append(name.text.strip())
# print(dog_names)



url = 'https://petstime.ru/article/krasivye-imena-dlya-ptits-malchikov-i-devochek'
headers = {'User-Agent': UserAgent().random}
html = requests.get(url, headers=headers)
names = soup(html.content, 'html.parser').select('div.entry-content.clearfix')[0].select('ul')[-9]
bird_names = []
for name in names:
    if name.text != '\n':
        bird_names.append(name.text.strip()[0:-1])
# print(bird_names)




##########PREMISE
print('''
Добро пожаловать в игру Магазин Животных!

Вам предстоит придумать название своего магазина и внести свой первый капитал!
Вы всегда можете посмотреть свой бюджет и список животных - для этого ничего не требуется.
Однако игра по-настоящему начинается только тогда, когда Вы решите не просто смотреть :D

Чтобы купить или продать животное, Вам нужно сходить на рынок, а рынок далеко!
На поход туда-обратно у Вас уйдет целый день, а аренда магазина стоит денег...
И ведь никто не гарантирует, что поход будет удачным.

Но есть и хорошие новости!
Опираясь на Вашу удачу, Вы вполне можете продать зверушку дороже, чем купили.
''')

# CONFIG/DEFAULTS
name = input('Придумай название магазина животных: ')

budget = 0 #1000
while budget == 0:
    try:
        budget = int(input('Введи стартовый капитал: '))
    except ValueError:
        print('Это не число')

#MODIFIERS
rent = int(0.05 * budget)

cat_a = int(0.01 * budget)
cat_b = int(0.2 * budget)

dog_a = int(0.5 * budget)
dog_b = int(1 * budget)

bird_a = int(1 * budget)
bird_b = int(2 * budget)

s = Shop(name,budget,[])


#GAME CYCLE
while True:
    print()
    print(f'0. Выйти из игры\n'
          f'1. Посмотреть бюджет\n'
          f'2. Посмотреть список животных\n'
          f'3. Купить животное на рынке\n'
          f'4. Продать животное на рынке\n'
          )

    try:
        option = int(input('Выбери, что ты хочешь сделать?: '))

        if option == 0:
            print(f'Магазин {s.name} закрывается...')
            quit()

        elif option == 1:
            print(f'Бюджет магазина {s.name} = {s.budget}')

        elif option == 2:
            ...

        # BUY
        elif option == 3:
            ...

        # SELL
        elif option == 4:
            ...



    except ValueError:
        print('Такой функции нет')