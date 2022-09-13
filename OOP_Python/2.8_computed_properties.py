# Создайте класс Rectangle, у которого есть:

# 1.конструктор __init__, принимающий 2 аргумента: длину и ширину. 
# 2.свойство area, которое возвращает площадь прямоугольника;

class Rectangle:

    def __init__(self, a, b):
        self.length = a
        self.width = b
    
    @property
    def area(self):
        return self.length*self.width


r1 = Rectangle(3, 5)
r2 = Rectangle(6, 1)

print(r1.area) # 15
print(r2.area) # 6


# Создайте класс Date, у которого есть:

# конструктор __init__, принимающий 3 аргумента: день, месяц и год. 
# свойство date , которое возвращает строку определенного формата "<день>/<месяц>/<год>";
# свойство usa_date, которое возвращает строку определенного формата "<месяц>-<день>-<год>";

class Date:

    def __init__(self, d, m, y):
        self.day = d
        self.month = m
        self.year = y

    @property
    def date(self):
        return f'{self.day:02}/{self.month:02}/{self.year:04}'

    @property
    def usa_date(self):
        return f'{self.month:02}-{self.day:02}-{self.year:04}'
    
    
d1 = Date(5, 10, 2001)
d2 = Date(15, 3, 999)

print(d1.date) # 05/10/2001
print(d1.usa_date) # 10-05-2001
print(d2.date) # 15/03/0999
print(d2.usa_date) # 03-15-0999