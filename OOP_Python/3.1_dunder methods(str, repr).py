# Создайте класс Person, у которого есть:

# 1. конструктор __init__, принимающий 3 аргумента: name, surname, gender. 
# Атрибут gender может принимать только 2 значения: "male" и "female", по умолчанию "male".
# Если в атрибут gender передается любое другое значение, печатать сообщение: "Не знаю, что вы имели ввиду?
# Пусть это будет мальчик!" и проставить атрибут gender значением "male"
# 2. переопределить метод __str__ следующим образом: 
# если объект - мужчина (атрибут gender = "male"), возвращать строку "Гражданин <Фамилия> <Имя>
# если объект - женщина (атрибут gender = "female"), возвращать строку "Гражданка <Фамилия> <Имя>


class Person:
    
    def __init__(self, name, surname, gender='male'):
        self.name = name
        self.surname = surname
        if gender in ['male', 'female']:
            self.gender = gender
        else:
            self.gender = 'male'
            print('Не знаю, что вы имели ввиду? Пусть это будет мальчик!')
    
    
    def __str__(self):
        if self.gender == 'male':
            return f'Гражданин {self.surname} {self.name}'
        else:
            return f'Гражданка {self.surname} {self.name}'


p1 = Person('Chuck', 'Norris')
print(p1)
print(p1.__dict__)

p2 = Person('Mila', 'Kunis', 'female')
print(str(p2))
print(p2.__dict__)

p3 = Person('Оби-Ван', 'Кеноби', True)
print(p3)




#  Создайте класс Vector, который хранит в себе вектор целых чисел.  У класса Vector есть:

# 1. конструктор __init__, принимающий произвольное количество аргументов. Среди всех переданных аргументов
# необходимо оставить только целые числа и сохранить их в атрибут values в виде списка;
# 2. переопределить метод __str__ так, чтобы экземпляр класса Vector выводился следующим образом: 
# -  "Вектор(<value1>, <value2>, <value3>, ...)", если вектор не пустой. При этом значения должны быть упорядочены
# по возрастанию (будьте аккуратнее с пробелами, они стоят только после запятых, см. пример ниже);
# - "Пустой вектор", если наш вектор не хранит в себе значения


class Vector:
    
    def __init__(self, *args):
        self.values = sorted(list(filter(lambda value: type(value) == int, args)))
        
    def __str__(self):
        if self.values:
            return f'Вектор{tuple(self.values)}'
        else:
            return 'Пустой вектор'
            
    
    

v1 = Vector(3,2,1,'a','c')
print(v1)

v2 = Vector()
print(v2) # печатает "Пустой вектор"
