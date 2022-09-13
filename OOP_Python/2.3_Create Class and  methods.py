# Создайте класс Dog, у которого есть:

# 1. метод __init__, принимающий имя и возраст собаки и сохраняющий их в аргументы name и age
# 2. метод description, который возвращает строку в виде «{name} is {age} years old»
# 3. метод speak принимающий один аргумент, который возвращает строку вида «{name} says {sound}»

class Dog:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    def description(self):
        return f'{self.name} is {self.age} years old'
    
    def speak(self, sound):
        self.sound = sound
        return f'{self.name} says {self.sound}'


jack = Dog("Jack", 4)

print(jack.description()) # распечатает 'Jack is 4 years old'
print(jack.speak("Woof Woof")) # распечатает 'Jack says Woof Woof'
print(jack.speak("Bow Wow")) # распечатает 'Jack says Bow Wow'



# Ваша задача реализовать класс Stack, у которого есть:

# 1. метод __init__создаёт новый пустой стек. Параметры данный метод не принимает. Создает атрибут экземпляра values, где будут в дальнейшем
# хранятся элементы стека в виде списка (list), изначально при инициализации задайте значение атрибуту values равное пустому списку;
# 2. метод push(item) добавляет новый элемент на вершину стека, метод ничего не возвращает.
# 3. метод pop() удаляет верхний элемент из стека. Параметры не требуются, метод возвращает элемент. Стек изменяется. 
# Если пытаемся удалить элемент из пустого списка, необходимо вывести сообщение "Empty Stack";
# 4. метод peek() возвращает верхний элемент стека, но не удаляет его. Параметры не требуются, стек не модифицируется. 
# Если элементов в стеке нет, распечатайте сообщение "Empty Stack", верните None после этого;
# 5. метод is_empty() проверяет стек на пустоту. Параметры не требуются, возвращает булево значение.
# 6. метод size() возвращает количество элементов в стеке. Параметры не требуются, тип результата - целое число.


class Stack:
    def __init__(self):
        self.values = []
    
    # метод push(item) добавляет новый элемент на вершину стека
    def push(self, item):
        self.values.append(item)
    
    # метод pop() удаляет верхний элемент из стека
    def pop(self):
        if len(self.values) == 0:
            print('Empty Stack')
        return self.values.pop()
    
    # метод peek() возвращает верхний элемент стека
    def peek(self):
        if len(self.values) == 0:
            print('Empty Stack')
            return None
        else:
            return self.values[-1]
    
    # метод is_empty() проверяет стек на пустоту
    def is_empty(self):
        return len(self.values) == 0
    
    # метод size() возвращает количество элементов в стеке
    def size(self):
        return len(self.values)
    
    
s = Stack()
s.peek()  # распечатает 'Empty Stack'
print(s.is_empty())  # распечатает True
s.push('cat')  # кладем элемент 'cat' на вершину стека
print(s.__dict__)
s.push('dog')  # кладем элемент 'dog' на вершину стека
print(s.__dict__)
print(s.peek())  # распечатает 'dog'
s.push(True)  # кладем элемент True на вершину стека
print(s.__dict__)
print(s.size())  # распечатает 3
print(s.is_empty())  # распечатает False
s.push(777)  # кладем элемент 777 на вершину стека
print(s.__dict__)
print(s.pop())  # удаляем элемент 777 с вершины стека и печатаем его
print(s.__dict__)
print(s.pop())  # удаляем элемент True с вершины стека и печатаем его
print(s.__dict__)
print(s.size())  # распечатает 2



# Создайте класс Worker, у которого есть:

# 1. метод __init__, принимающий 4 аргумента: имя, зарплата, пол и паспорт. Необходимо сохранить их в
# следующих атрибутах: name, salary, gender и passport.
# 2. свойство get_info, которое распечатает информацию о сотруднике в следующем виде:
# «Worker {name}; passport-{passport}»

# Ниже имеется список кортежей persons, содержащий информацию о десяти работниках. Ваша задача на основании persons
# создать список worker_objects, в котором необходимо добавить десять экземпляров класса Worker. Работников в списке
# следует разместить в том же порядке, в каком они встречаются в списке persons. В этом же порядке для каждого объекта
# в списке worker_objects вызовите метод get_info

class Worker:
    def __init__(self, name, salary, gender, passport):
        self.name = name
        self.salary = salary
        self.gender = gender
        self.passport = passport
    
    def get_info(self):
        print(f'Worker {self.name}; passport-{self.passport}')


persons= [
    ('Allison Hill', 334053, 'M', '1635644202'),
    ('Megan Mcclain', 191161, 'F', '2101101595'),
    ('Brandon Hall', 731262, 'M', '6054749119'), 
    ('Michelle Miles', 539898, 'M', '1355368461'),
    ('Donald Booth', 895667, 'M', '7736670978'), 
    ('Gina Moore', 900581, 'F', '7018476624'),
    ('James Howard', 460663, 'F', '5461900982'), 
    ('Monica Herrera', 496922, 'M', '2955495768'),
    ('Sandra Montgomery', 479201, 'M', '5111859731'), 
    ('Amber Perez', 403445, 'M', '0602870126')
]


worker_objects = [Worker(*i) for i in persons]

# for i in worker_objects:
#     print(i.get_info())

for i in worker_objects:
    print(Worker.get_info(i))



# Задание
# Ваша задача  создать класс CustomLabel, у которого есть:

# 1. метод __init__, принимающий один обязательный аргумент текст виджета, его необходимо сохранить в атрибут text.
# И также в метод  может поступать произвольное количество именованных аргументов. Их необходимо сохранять в атрибуты
# экземпляра под тем же названием
# 2. метод config, который принимает произвольное количество именованных атрибутов. Он должен создать атрибут с 
# указанным именем или, если этот атрибут уже присутствовал в экземпляре, изменить его на новое значение


class CustomLabel:
    def __init__(self, text, **kwargs):
        self.text = text
        for key, value in kwargs.items():
            setattr(self, str(key), value)
    
    def config(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, str(key), value)   

label = CustomLabel(text="Hello", bd=20, bg='#ffaaaa')

print(label.__dict__) # {'text': 'Hello', 'bd': 20, 'bg': '#ffaaaa'}

label.config(color='red', bd=100)

print(label.__dict__) # {'text': 'Hello', 'bd': 100, 'bg': '#ffaaaa', 'color': 'red'}




# Создайте базовый класс Person, у которого есть:
# 1. метод __init__, принимающий имя и возраст человека. Их необходимо сохранить в атрибуты экземпляра nameи age соответственно
# 2. метод display_person_info , который печатает информацию в следующем виде: Person: {name}, {age}

# Затем создайте класс Company , у которого есть:
# 1. метод __init__, принимающий название компании и город ее основания. Их необходимо сохранить в атрибуты экземпляра company_name и location соответственно
# 2. метод display_company_info , который печатает информацию в следующем виде: Company: {company_name}, {location}

# И в конце создайте класс Employee , который:
# 1. имеет метод __init__, принимающий название имя человека, его возраст, название компании и город основания. 
# Необходимо создать атрибут personal_data и сохранить в него экземпляр класса Person. И также создать атрибут work  и сохранить в него экземпляр класса Company
 
# После этого через атрибуты personal_data и work  вы можете обращаться к методам соответствующих классов Person и Company 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_person_info(self):
        print(f'Person: {self.name}, {self.age}')


class Company:
    def __init__(self, company_name, location):
        self.company_name = company_name
        self.location = location
    
    def display_company_info(self):
        print(f'Company: {self.company_name}, {self.location}')


class Employee:
    def __init__(self, name, age, company_name, location):
        self.personal_data = Person(name, age)
        self.work = Company(company_name, location)


emp = Employee('Jessica', 28, 'Google', 'Atlanta')
print(emp.personal_data.name)
print(emp.personal_data.age)
emp.personal_data.display_person_info()
print(emp.work.company_name)
print(emp.work.location)
emp.work.display_company_info()        