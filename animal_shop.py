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
