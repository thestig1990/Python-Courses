# Создайте класс Student, у которого есть:

# 1. конструктор __init__, принимающий 3 аргумента и создает приватные атрибуты __name, __age, __branch;
# 2. приватный метод __display_details , который выводит на экран информацию о студенте в следующем виде
# Имя: <name>
# Возраст: <age>
# Направление: <branch>
# 3. метод access_private_method, который вызывает приватный метод __display_details

class Student:
    def __init__(self, name, age, branch):
        self.__name = name
        self.__age = age
        self.__branch = branch
    
    def __display_details(self):
        print(f'Имя: {self.__name}', f'Возраст: {self.__age}', f'Направление: {self.__branch}', sep='\n')
    
    def access_private_method(self):
        self.__display_details()


obj = Student("Adam Smith", 25, "Information Technology")
obj.access_private_method()


# В этом задании научимся просто вызывать защищенные и приватные методы у экземпляров класса.
# Представьте, у вас есть вот такой класс:
# Ваша задача вызвать у экземпляра класса maker сперва метод _make_barbecue , затем метод __make_pepperoni

class PizzaMaker:
    def __make_pepperoni(self):
        print('print private method')


    def _make_barbecue(self):
        print('print protected method')


print(PizzaMaker.__dict__.keys())

maker = PizzaMaker()
maker._make_barbecue()
#maker._PizzaMaker__make_pepperoni()


help(isinstance)