class Animal:
    def __init__(self, name, price):
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
    def __init__(self, name, budget, animals):
        self.name = name
        self.animals = animals
        self.budget = budget

    def __str__(self):
        return f'Бюджет магазина {self.name}: {self.budget}'

    def buy_animal(self, animal):
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