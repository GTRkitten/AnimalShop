class Animal:
    def __init__(self, name:str, price:int, date) -> None:
        self.name = name
        self.price = price

        self.date = date
        self.weight = 1
        self.modifier = 0.01  # MODIFIER
        self.rarity = self.weight * self.modifier

    def value(self, date:int) -> None:
        price = self.price
        self.price += price * self.rarity * (date - self.date)

    def sound(self) -> str:
        return f'Звук'


class Cat(Animal):
    def __init__(self, name, price, date) -> None:
        super().__init__(name, price, date)
        self.weight = 1
        self.modifier = 0.01  # MODIFIER

    def sound(self) -> str:
        super().sound()
        return f'Мяууу!'

class Dog(Animal):
    def __init__(self, name, price, date) -> None:
        super().__init__(name, price, date)
        self.weight = 5/3
        self.modifier = 0.01  # MODIFIER

    def sound(self) -> str:
        super().sound()
        return f'Гав!'


class Bird(Animal):
    def __init__(self, name, price, date) -> None:
        super().__init__(name, price, date)
        self.weight = 5/2
        self.modifier = 0.01 #MODIFIER

    def sound(self) -> str:
        super().sound()
        return f'Чирик-чирик!'


class Shop:
    def __init__(self, name:str,
                 budget:int,
                 animals:list) -> None:
        self.name = name
        self.animals = animals
        self.budget = budget

    def __str__(self) -> str:
        return f'Бюджет магазина {self.name}: {self.budget}'

    def buy_animal(self, animal:Animal) -> None:
        if self.budget >= animal.price:
            self.budget -= animal.price
            self.animals.append(animal)
            print(animal.sound())
        else:
            print(f'На покупку {animal.name} у {self.name} недостаточно денюжек :(')

    def sell_animal(self, animal) -> None:
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


#TRACK SYSTEM
day = 1
score = 0

#GAME CYCLE
while True:
    # HOLD MECHANIC
    if len(s.animals) > 0:
        for animal in s.animals:
            animal.value(day)
            animal.date = day

    if s.budget > score and s.budget > budget:
        score = s.budget - budget

    print()
    print(f'0. Выйти из игры\n'
          f'1. Посмотреть бюджет\n'
          f'2. Посмотреть прибыль относительно начального капитала\n'
          f'3. Посмотреть список животных\n'
          f'4. Купить животное на рынке\n'
          f'5. Продать животное на рынке\n'
          )

    try:
        option = int(input('Выбери, что ты хочешь сделать?: '))

        if option == 0:
            print(f'Магазин {s.name} закрывается...')
            quit()

        elif option == 1:
            print(f'Бюджет магазина {s.name} = {s.budget}')

        elif option == 2:
            print(f'Ваша прибыль составляет {s.budget - budget}')

        elif option == 3:
            print(f'Список животных магазина {s.name}: \n')
            if len(s.animals) > 0:
                for i, animal in enumerate(s.animals):
                    print(f'{i + 1}){animal.name} стоимостью {animal.price}')
                print()
            else:
                print(f'В магазине "{s.name}" пока нет животных')

        # BUY
        elif option == 4:
            market = []
            for i in range(randint(2, 5)):
                market.append(choices([
                    Cat(cat_names[randint(0, len(cat_names) - 1)], randint(cat_a, cat_b), day),
                    Dog(dog_names[randint(0, len(dog_names) - 1)], randint(dog_a, dog_b), day),
                    Bird(bird_names[randint(0, len(bird_names) - 1)], randint(bird_a, bird_b), day)],
                    weights=[0.5, 0.3, 0.2],  # MODIFIER
                    k=1)[0])
            print(f'День: {day}. Вы заплатите за аренду магазина {rent} денег')
            print(f'На рынке сейчас есть:\n')
            for i in range(len(market)):
                print(f'{i + 1}. Купить "{market[i].name}" за {market[i].price}: {market[i].sound()}\n')
            print(f'0. Пропустить день\n')

            # SELECTION
            try:
                buy = int(input('Кого Вы хотите купить?: ')) - 1
                if buy in range(len(market)):
                    s.buy_animal(market[buy])
                    s.budget -= rent
                    day += 1
                else:
                    print(f'Вы пошли на рынок и вернулись ни с чем')
                    s.budget -= rent
                    day += 1
            except ValueError:
                print(f'На рынке такого нет!')
                s.budget -= rent
                day += 1

        # SELL
        elif option == 5:
            print(f'День: {day}. Вы заплатили за аренду магазина {rent} денег')
            if len(s.animals) > 0:
                try:
                    sell = int(input('Выберите номер зверушки на продажу: ')) - 1
                    if sell in range(len(s.animals)):
                        r = s.animals[sell].price

                        if s.animals[sell].__class__.__name__ == 'Cat':
                            s.animals[sell].price = randint(int(r / 4), int(r * 3))  # MODIFIER

                        elif s.animals[sell].__class__.__name__ == 'Dog':
                            s.animals[sell].price = randint(int(r / 3), int(r * 2))  # MODIFIER

                        else:
                            s.animals[sell].price = randint(int(r / 2), int(r * 1.5))  # MODIFIER

                        print(f'Вы продали {s.animals[sell].name} за {s.animals[sell].price}')
                        s.sell_animal(s.animals[sell])
                        s.budget -= rent
                        day += 1

                    else:
                        print('Вы так торопились на рынок, что не взяли с собой зверушку!')
                        s.budget -= rent
                        day += 1

                except ValueError:
                    print('Вы так торопились на рынок, что не взяли с собой зверушку!')
                    s.budget -= rent
                    day += 1
            else:
                print(f'Вам нечего продать на рынке. День прошел зря')
                s.budget -= rent
                day += 1

        else:
            print('Такой функции нет')

        if s.budget <= 0 and len(s.animals) == 0:
            print('Вы разорились :(')
            break
    except ValueError:
        print('Такой функции нет')

print(f'Вы пробыли владельцем {s.name} {day} дней и стали богаче в {score} раз!')
