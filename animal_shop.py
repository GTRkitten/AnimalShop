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


# url = 'https://zoo-perm.ru/novosti/krasivye-imena-dlya-koshek-putevoditel-po-vyboru-idealnogo-imeni-dlya-vashego-pushistogo-druga/'
# headers = {'User-Agent': UserAgent().random}
# html = requests.get(url, headers=headers)
# names = soup(html.content, 'html.parser')
# c_names = names.select('blockquote')[1].text.strip('').split()
# cat_names = []
# for name in c_names:
#     cat_names.append(name[0:-1])
# print(cat_names)
cat_names = ['Барабашка', 'Бублик', 'Ватрушка', 'Вафля', 'Варенье', 'Винни', 'Винтик', 'Винегрет', 'Гном', 'Дыня', 'Жвачка', 'Зайка', 'Ириска', 'Капуста', 'Карамелька', 'Кефир', 'Кекс', 'Клешня', 'Козявка', 'Компот', 'Конфетка', 'Коржик', 'Котлета', 'Лимончик', 'Мафин', 'Мармеладка', 'Няшка', 'Оладушка', 'Пампушка', 'Пельмень', 'Пельмешка', 'Пышка', 'Пыжик', 'Пузырь', 'Пупсик', 'Пышечка', 'Рагу', 'Рыжик', 'Сарделька', 'Сосиска', 'Сырник', 'Творожок', 'Фрикаделька', 'Хвостик', 'Цыпленок', 'Шарик', 'Шпрот', 'Эскимо', 'Ягодка']


# url = 'https://www.purinaone.ru/dog/articles/new-owner-tips/klichki-dlya-sobak-malchikov'
# headers = {'User-Agent': UserAgent().random}
# html = requests.get(url, headers=headers)
# names = soup(html.content, 'html.parser').select('table')[1].select('p')
# dog_names = []
# for name in names:
#     dog_names.append(name.text.strip())
# print(dog_names)
dog_names = ['Босс', 'Кудряш', 'Пикачу', 'Буян', 'Кукис', 'Пират', 'Воланд', 'Лексус', 'Питон', 'Гаврик', 'Лунтик', 'Пряник', 'Гуффи', 'Мамай', 'Рембо', 'Доллар', 'Мистер', 'Тайсон', 'Дракула', 'Модник', 'Царь', 'Дюшес', 'Ниндзя', 'Шнапс', 'Изюм', 'Ньютон', 'Шредер', 'Йода', 'Оливье', 'Шрек', 'Коржик', 'Оби-Ван', 'Шумахер']


# url = 'https://petstime.ru/article/krasivye-imena-dlya-ptits-malchikov-i-devochek'
# headers = {'User-Agent': UserAgent().random}
# html = requests.get(url, headers=headers)
# names = soup(html.content, 'html.parser').select('div.entry-content.clearfix')[0].select('ul')[-9]
# bird_names = []
# for name in names:
#     if name.text != '\n':
#         bird_names.append(name.text.strip()[0:-1])
# print(bird_names)
bird_names = ['Абду', 'Бибигон', 'Бисер', 'Винтик', 'Глюк', 'Жулик', 'Йорк', 'Йо-йо', 'Крекер', 'Крош', 'Лунтик', 'Лютик', 'Минипут', 'Немо', 'Пивз', 'Покемон', 'Твикс', 'Ферби', 'Флик', 'Флэш', 'Чипс', 'Щипун', 'Эвон', 'Юнга', 'Янг']


############IMPORTS
from random import randint
from random import choices

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
rent = int(0.01 * budget)
print(f'\nАренда магазина обойдется Вам в {rent}\n')

cat_a = int(0.05 * budget)
cat_b = int(0.25 * budget)

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
            print(f'Список животных магазина {s.name}: ')
            if len(s.animals) > 0:
                for animal in s.animals:
                    print(animal.name, end=' ')
                print()
            else:
                print(f'В магазине "{s.name}" пока нет животных')

        # BUY
        elif option == 3:
            market = choices([Cat(cat_names[randint(0, len(cat_names) - 1)], randint(cat_a, cat_b)),
                              Dog(dog_names[randint(0, len(dog_names) - 1)], randint(dog_a, dog_b)),
                              Bird(bird_names[randint(0, len(bird_names) - 1)], randint(bird_a, bird_b)), ],
                             weights=[0.5, 0.3, 0.2],  # MODIFIER
                             k=5)
            print(f'На рынке сейчас есть:\n')
            for i in range(len(market)):
                print(f'{i + 1}. Купить "{market[i].name}" за {market[i].price}\n')
            print(f'0. Пропустить день\n')

            # CHOICE
            try:  # здесь такая же шляпа
                choice = int(input('Кого Вы хотите купить?: ')) - 1
                if choice in range(len(market)):
                    s.buy_animal(market[choice])
                    s.budget -= rent
                else:
                    print(f'Вы пошли на рынок и вернулись ни с чем')
                    s.budget -= rent
            except ValueError:
                print(f'На рынке такого нет!')
                s.budget -= rent

        # SELL
        elif option == 4:
            if len(s.animals) > 0:
                try:
                    sell = int(input('Выберите номер зверушки на продажу: ')) - 1
                    if sell in range(len(s.animals)):
                        r = s.animals[sell].price
                        if s.animals[sell].__class__.__name__ == 'Cat':
                            s.animals[sell].price = randint(int(r / 4), int(cat_b * 2))  # MODIFIER

                        elif s.animals[sell].__class__.__name__ == 'Dog':
                            s.animals[sell].price = randint(int(r / 3), int(dog_b * 1.5))  # MODIFIER

                        else:
                            s.animals[sell].price = randint(int(r / 2), int(bird_b * 1.2))  # MODIFIER

                        s.sell_animal(s.animals[sell])
                        s.budget -= rent
                        print(f'Вы продали зверушку под номером {sell + 1}')
                    else:
                        print('Вы так торопились на рынок, что не взяли с собой зверушку!')
                        s.budget -= rent

                except ValueError:
                    print('Вы так торопились на рынок, что не взяли с собой зверушку!')
                    s.budget -= rent
            else:
                print(f'Вам нечего продать на рынке. День прошел зря')
                s.budget -= rent
        else:
            print('Такой функции нет')

        if s.budget <= 0 and len(s.animals) == 0:
            print('Вы разорились :(')
            quit()
    except ValueError:
        print('Такой функции нет')