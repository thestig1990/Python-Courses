# Создайте класс Lion. В нем должен быть метод roar, который печатает на экран "Rrrrrrr!!!"
# Необходимо написать только определение класса

from cmath import pi


class Lion:
    def roar(self):
        print('Rrrrrrr!!!')

simba = Lion()
simba.roar()    # печатает Rrrrrrr!!!


# Создайте класс Robot, в котором реализованы:
# 1. метод say_hello , печатающий на экран фразу «Hello, human! My name is C-3PO»
# 2. метод say_bye ,  печатающий на экран фразу «See u later alligator»

# После определения класса создайте 2 экземпляра и сохраните их в переменные  c3po и r2d2
# Затем вызовите у переменной  c3po сперва метод say_hello , а затем метод say_bye 
# И тоже самое сделайте с переменной r2d2: сперва вызывайте метод say_hello , потом - метод say_bye

class Robot:
    def say_hello(self):
        print('Hello, human! My name is C-3PO')
        
    def say_bye(self):
        print('See u later alligator')

c3po = Robot()
r2d2 = Robot()

c3po.say_hello()
c3po.say_bye()

Robot.say_hello(r2d2)
Robot.say_bye(r2d2)


# В предыдущей задачи вы могли обратить внимание на то, что выводится всегда одно и тоже имя робота в методе say_hello.
# Давайте это исправим при помощи атрибута экземпляра name . Для этого переопределяем класс Robot, в котором должны быть реализованы

# метод set_name , принимающий имя робота и сохраняющий его в атрибуте экземпляра name 
# метод say_hello , Метод должен проверить, если у ЭК атрибут name . Если атрибут name  присутствует, необходимо напечатать фразу
# «Hello, human! My name is <name>». Если атрибут name  отсутствует у экземпляра, печатайте сообщение «У робота нет имени» 
# метод say_bye ,  печатающий на экран фразу «See u later alligator»

class RobotNew:
    def set_name(self, name):
        self.name = name

    def say_hello(self):
        if hasattr(self, 'name'):
            print(f'Hello, human! My name is {self.name}')
        else:
            print('У робота нет имени')
        
    def say_bye(self):
        print('See u later alligator')


c3po1 = RobotNew()
c3po1.say_hello() # печатает У робота нет имени
c3po1.set_name('R2D2') 
c3po1.say_hello() # печатает Hello, human! My name is R2D2
c3po1.say_bye() # печатает See u later alligator

r = RobotNew()
r.set_name('Chappy')
r.say_hello()# печатает Hello, human! My name is Chappy



# Создайте класс Counter, экземпляры которого будут подсчитывать внутри себя значения.

# В классе Counter нужно определить метод start_from, который принимает один необязательный аргумент - значение,
# с которого начинается подсчет, по умолчанию равно 0

# Также нужно создать метод increment, который увеличивает счетчик на 1.

# Затем необходимо создать метод display, который печатает фразу "Текущее значение счетчика = <value>" и метод reset,
# который обнуляет экземпляр счетчика


class Counter:
    def start_from(self, start=0):
        self.start = start
    
    def increment(self):
        self.start += 1
    
    def display(self):
        print(f'Текущее значение счетчика = {self.start}')
    
    def reset(self):
        self.start = 0


c1 = Counter()
c1.start_from()
c1.increment()
c1.display()    # печатает "Текущее значение счетчика = 1"
c1.increment()
c1.display()    # печатает "Текущее значение счетчика = 2"
c1.reset()
c1.display() # печатает "Текущее значение счетчика = 0"

c2 = Counter()
c2.start_from(3)
c2.display() # печатает "Текущее значение счетчика = 3"
c2.increment()
c2.display() # печатает "Текущее значение счетчика = 4"

print(c1.__dict__)
print(c2.__dict__)
print(Counter.__dict__)
print(getattr(Counter, 'self.start', 'do not have attributes'))
print(hasattr(Counter, 'self.start'))



# Создайте класс Constructor, в котором реализованы

# метод add_atribute , принимающий на вход название атрибута в виде строки и его значение. 
# При помощи функции setattr необходимо создать или изменить атрибут для ЭК, у которого этот метод был вызван
# метод display ,  печатающий на экран словарь __dict__ у ЭК

#VAR1
class Constructor:
    def add_atribute(self, name, value):
        setattr(self, name, value)
    def display(self):
        print(self.__dict__)

        
obj1 = Constructor()
obj1.display() # печатает {}
obj1.add_atribute('color', 'red')
obj1.add_atribute('width', 20)
obj1.display() # печатает {'color': 'red', 'width': 20}

obj2 = Constructor()
obj2.display() # печатает {}
obj2.add_atribute('height', 100)
obj2.display() # печатает {'height': 100}



#VAR2
class ConstructorNew:
    def add_atribute(self, value):
        self.name = value
    def display(self):
        print(self.__dict__)

obj3 = Constructor()
obj3.display() # печатает {}
obj3.add_atribute('color', 'red')
obj3.add_atribute('width', 20)
obj3.display() # печатает {'color': 'red', 'width': 20}

obj4 = Constructor()
obj4.display() # печатает {}
obj4.add_atribute('height', 100)
obj4.display() # печатает {'height': 100}



# Создайте класс Point. У этого класса должны быть

# метод set_coordinates, который принимает координаты по x и по y, и сохраняет их в экземпляр класса соответственно в атрибуты x и y 
# метод get_distance, который обязательно принимает экземпляр класса Point и возвращает расстояние между двумя точками по теореме Пифагора.
# В случае, если в данный метод передается не экземпляр класса Point необходимо вывести сообщение "Передана не точка"

class Point:
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y
        print(f'Coordinates: ({self.x}, {self.y})')
        
    def get_distance(self, instance):
        if isinstance(instance, Point):
            distance = ((instance.x - self.x)**2 + (instance.y - self.y)**2)**0.5
            return f'Distance between 2 points - {distance}'
        else:
            print('Передана не точка')


          
p1 = Point()
p2 = Point()
p1.set_coordinates(1, 2)
p2.set_coordinates(4, 6)

print(p1.x, p1.y)
print(p2.x, p2.y)

print(p1.get_distance(p2))

p1.get_distance(10)