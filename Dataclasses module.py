# Модуль dataclass. Data-классы
"""
Модуль dataclasses предоставляет декоратор dataclass, который 
позволяет создавать data-классы - подобные позволяют значительно 
сократить шаблонный код классов. Как правило, такие классы 
предназначены для хранения некоторого состояния, некоторых данных 
и когда не требуется какое-то поведение в виде функций.
"""

# обычный класс
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

tom = Person("Tom", 38)
print(f"Name: {tom.name}  Age: {tom.age}") # Name: Tom  Age: 38

# применим модуль
# импортируем из модуля dataclasses декоратор dataclass
from dataclasses import dataclass 

@dataclass
class Person: # уже не надо указывать конструктор - функцию __init__, просто указываем атрибуты
    name: str
    age: int

# А Python потом сам сгенерирует конструктор, в который также 
# мы можем передать значения для атрибутов объекта

tom = Person("Tom", 38)
print(f"Name: {tom.name}  Age: {tom.age}") # Name: Tom  Age: 38

"""
Генерацией метода __init__ функциональность декоратора dataclass 
не ограничивается. В реальности data-класс будет аналогичен следующему:
"""

"""
class Person:
    def __init__(self, name, age):  # конструктор
        self.name = name
        self.age = age
 
    def __repr__(self): # функция __repr__() для возвращения строкового представления
        return f"Person(name={self.name!r}, age={self.age!r}"
     
    def __eq__(self, other): # функция __eq__() для сравнения двух объектов
        if other.__class__ is self.__class__:
            return (self.name, self.age) == (other.name, other.age)
        return NotImplemented
"""

# ПРИМЕНЕНИЕ функций
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

tom = Person("Tom", 38)
bob = Person("Bob", 42)
tomas = Person("Tom", 38)
print(tom == tomas) # True
print(tom == bob)   # False
print(tom)          # Person(name="Tom", age=38)         


# Параметры декоратора dataclass
# С помощью параметров декоратор dataclass позволяет сгенерировать доп.
# шаблонный код и вообще настроить генерацию кода:
"""
def dataclass(cls=None, /, *, init=True, repr=True, eq=True, order=False,
              unsafe_hash=False, frozen=False, match_args=True,
              kw_only=False, slots=False)

init: если равно True, то генерируется функция __init__(). 
По умолчанию равно True

repr: если равно True, то генерируется функция __repr__(), 
которая возвращает строковое представление объекта. По умолчанию равно True

eq: если равно True, то генерируется функция __eq__(), 
которая сравнивает два объекта. По умолчанию равно True

order: если равно True, то генерируются функции __lt__ (операция <), 
__le__ (<=), __gt__ (>), __ge__ (>=), которые применяются для 
упорядочивания объектов. По умолчанию равно False

unsafe_hash: если равно True, то генерируется функция __hash__(), 
которая возвращает хеш объекта. По умолчанию равно False

Кроме того, те функции, которые создаются по умолчанию, МОГУТ БЫТЬ ПЕРЕОПРЕДЕЛЕНЫ.
"""
# Применение параметров
from dataclasses import dataclass

@dataclass(unsafe_hash=True, order=True) # включаем генерирование хеша, функциn упорядочивания
class Person:
    name: str
    age: int 
    def __repr__(self): # явным образом переопределяем функцию __repr__ для создания строкового представления объекта
        return f"Person. Name: {self.name}  Age: {self.age}"
    

tom = Person("Tom", 38)
print(tom.__hash__())    # -421667297069596717
print(tom)               # Person. Name: Tom  Age: 38

# значения по умолчанию
"""
При необходимости атрибутам можно присвоить значения по умолчанию, если в конструкторе им не передаются значения:
"""
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int = 18

tom = Person("Tom",38)  # Person(name="Tom", age=38)
print(tom)

bob = Person("Bob")     # Person(name="Bob", age=18)
print(bob)

# Добавление дополнительного функционала
"""
Хотя data-классы предназначены прежде всего для хранения различных данных, но также в них можно
определять поведение с помощью дополнительных функций:
"""
from dataclasses import dataclass
 
@dataclass
class Person:
    name: str
    age: int
 
    def say_hello(self):
        print(f"{self.name} says hello")
 
 
tom = Person("Tom", 38)
tom.say_hello()     # Tom says hello