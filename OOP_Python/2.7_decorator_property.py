# Создайте класс Notebook, у которого есть:

# конструктор __init__, принимающий 1 аргумента: список записей, в принципе там могут быть любые значения. 
# Необходимо сохранить его в защищенном атрибуте ._notes
# свойство notes_list, которое распечатает содержимое атрибута ._notes в виде упорядоченного списка (см. пример ниже)

class Notebook:
    def __init__(self, notes):
        self._notes = notes
    
    @property
    def notes_list(self):
        for i in range(len(self._notes)):
            print(f'{i+1}.{self._notes[i]}')
    

note = Notebook(['Buy Potato', 'Buy Carrot', 'Wash car'])
note.notes_list




#    Создайте класс Money, у которого есть:

# 1.конструктор __init__, принимающий 2 аргумента: dollars, cents. По входным аргументам вам необходимо создать атрибут экземпляра total_cents. 
# 2.свойство геттер dollars, которое возвращает количество имеющихся долларов;
# 3.свойство сеттер dollars, которое принимает целое неотрицательное число - количество долларов и устанавливает при помощи него новое значение в атрибут экземпляра total_cents, при этом значение центов должно сохранятся. В случае, если в сеттер передано число, не удовлетворяющее условию, нужно печатать на экран сообщение "Error dollars";
# 4.свойство геттер cents, которое возвращает количество имеющихся центов;
# 5.свойство сеттер cents, которое принимает целое неотрицательное число меньшее 100 - количество центов и устанавливает при помощи него новое значение в атрибут экземпляра total_cents, при этом значение долларов должно сохранятся. В случае, если в сеттер передано число, не удовлетворяющее условию, нужно печатать на экран сообщение "Error cents";
# 6.метод __str__ (информация по данному методу), который возвращает строку вида "Ваше состояние составляет {dollars} долларов {cents} центов". Для нахождения долларов и центов в методе __str__ пользуйтесь свойствами
# В экземпляр класса кроме атрибута total_cents сохранять ничего не нужно!


class Money:

    def __init__(self, dollars, cents):
        self.total_cents = dollars*100 + cents
    
    @property
    def dollars(self):
        return self.total_cents // 100
    
    @dollars.setter
    def dollars(self, num_d):
        if isinstance(num_d, int) and num_d >= 0:
            self.total_cents = num_d*100 + self.total_cents % 100
        else:
            print('Error dollars')
            
    @property
    def cents(self):
        return self.total_cents % 100
    
    @cents.setter
    def cents(self, num_c):
        if isinstance(num_c, int) and 0 <= num_c < 100:
            self.total_cents = self.dollars*100 + num_c
        else:
            print('Error cents')
    
    def __str__(self):
        return f'Ваше состояние составляет {self.dollars} долларов {self.cents} центов'


Bill = Money(101, 99)
print(Bill)  # Ваше состояние составляет 101 долларов 99 центов
print(Bill.dollars, Bill.cents)  # 101 99
print(Bill.total_cents)  # 10199
Bill.dollars = 666
print(Bill)  # Ваше состояние составляет 666 долларов 99 центов
Bill.cents = 12
print(Bill)  # Ваше состояние составляет 666 долларов 12 центов

print(Bill.__dict__)