# Создайте класс Vehicle, у которого есть: конструктор __init__, принимающий максимальную скорость и пробег.
# Их необходимо сохранить в атрибуты экземпляра max_speed и mileage соответственно

from mimetypes import init
from re import S


class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

modelX = Vehicle(240, 18)
print(modelX.max_speed, modelX.mileage)



# Создайте класс Laptop, у которого есть:

# конструктор __init__, принимающий 3 аргумента: бренд, модель и цену ноутбука. 
# На основании этих аргументов нужно для экземпляра создать атрибуты brand, model, price 
# и также атрибут laptop_name - строковое значение, следующего вида: "<brand> <model>"

class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = brand + ' ' + model


laptop1 = Laptop('hp', '15-bw0xx', 14000)

laptop2 = Laptop('ASUS', 'Vivibook', 15999)

hp = Laptop('hp', '15-bw0xx', 57000)
print(hp.price) # выводит 57000
print(hp.laptop_name) # выводит "hp 15-bw0xx"



# Создайте класс SoccerPlayer, у которого есть:

# 1.конструктор __init__, принимающий 2 аргумента: name, surname. Также во время инициализации необходимо создать
# 2 атрибута экземпляра: goals и assists - общее количество голов и передач игрока, изначально оба значения должны быть 0.
# 2. метод score, который принимает количество голов, забитых игроком, по умолчанию данное значение равно единице.
# Метод должен увеличить общее количество забитых голов игрока на переданное значение;
# 3. метод make_assist, который принимает количество передач, сделанных игроком за матч, по умолчанию данное значение равно единице.
# Метод должен увеличить общее количество сделанных передач игроком на переданное значение;
# 4. метод statistics, который вывод на экран статистику игрока в виде:
# <Фамилия> <Имя> - голы: <goals>, передачи: <assists>


class SoccerPlayer:
    def __init__(self, name, surname, goals=0, assists=0):
        self.name = name
        self.surname = surname
        self.goals = goals
        self.assists = assists
    
    def score(self, quantity_goals=1):
        self.goals += quantity_goals
    
    def make_assist(self, quantity_assists=1):
        self.assists += quantity_assists
    
    def statistics(self):
        print(f'{self.surname} {self.name} - голы: {self.goals}, передачи: {self.assists}')



leo = SoccerPlayer('Leo', 'Messi')
leo.score(700)
leo.make_assist(500)
leo.statistics() # выводит "Messi Leo - голы: 700, передачи: 500"



# Создайте класс Zebra, внутри которого есть метод which_stripe , который поочередно печатает фразы "Полоска белая",
# "Полоска черная", начиная именно с фразы "Полоска белая"

#VAR1
class Zebra:
    count = 0
    def which_stripe(self):
        if self.count % 2 == 0:
            print('Полоска белая')
        else:
            print('Полоска черная')
        self.count += 1


z1 = Zebra()
z1.which_stripe() # печатает "Полоска белая"
z1.which_stripe() # печатает "Полоска черная"
z1.which_stripe() # печатает "Полоска белая"

z2 = Zebra()
z2.which_stripe() # печатает "Полоска белая"
z2.which_stripe() # печатает "Полоска черная"


#VAR2
class ZebraNew:

    def __init__(self):
        self.num = 0

    def which_stripe(self):
        self.num += 1
        print(["Полоска черная", "Полоска белая"][self.num % 2])


z3 = ZebraNew()
z3.which_stripe() # печатает "Полоска белая"
z3.which_stripe() # печатает "Полоска черная"
z3.which_stripe() # печатает "Полоска белая"




# Создайте класс Person, у которого есть:

# 1. конструктор __init__, принимающий имя, фамилию и возраст. Их необходимо сохранить в атрибуты экземпляра first_name, last_name, age. 
# 2. метод full_name, который возвращает строку в виде "<Фамилия> <Имя>"
# 3. метод is_adult, который возвращает True, если человек достиг 18 лет и False в противном случае.

class Person:
    def __init__(self, first_name, last_name, age):
        self.name = first_name
        self.surname = last_name
        self.age = age
    
    def full_name(self):
        return f'{self.surname} {self.name}'
    
    def is_adult(self):
        return self.age >= 18      
        
p1 = Person('Jimi', 'Hendrix', 55)
print(p1.full_name())  # выводит "Hendrix Jimi"
print(p1.is_adult()) # выводит "True"
