# Определение и подключение модулей
"""
Модуль в языке Python представляет 
отдельный файл с кодом, который можно повторно использовать 
в других программах.
По умолчанию интерпретатор Python ищет модули по ряду 
стандартных путей, один из которых - это папка главного, запускаемого скрипта.
"""

import Module # подключаем модуль Module.py

# выводим значение переменной hello
print(Module.hello)        # Hello all
# обращаемся к функции print_message
Module.print_message("Hello work")  # Message: Hello work

"""
Для использования модуля его надо импортировать с помощью оператора import, 
после которого указывается имя модуля: import message.
Чтобы обращаться к функциональности модуля, нам нужно получить его пространство
имен. По умолчанию оно будет совпадать с именем модуля, то есть в нашем случае 
также будет называться message.
Получив пространство имен модуля, мы сможем обратиться к его функциям по схеме
пространство_имен.функция
"""

# Подключение функциональности модуля в глобальное пространство имен
"""
Другой вариант настройки предполагает импорт функциональности модуля в глобальное 
пространство имен текущего модуля с помощью ключевого слова from:
"""
from Module import print_message
 
# обращаемся к функии print_message из модуля message
print_message("Hello work")  # Message: Hello work
 
# переменная hello из модуля message не доступна, так как она не импортирована
# print(message.hello)   
# print(hello) 

from Module import print_message
from Module import hello
 
# обращаемся к функции print_message из модуля message
print_message("Hello work")  # Message: Hello work
 
# обращаемся к переменной hello из модуля message
print(hello)    # Hello all

"""
Если необходимо импортировать в глобальное пространство имен весь функционал,
то вместо названий отдельных функций и переменных можно использовать символ зводочки *:
"""
from Module import *

# обращаемся к функции print_message из модуля message
print_message("Hello work")  # Message: Hello work
 
# обращаемся к переменной hello из модуля message
print(hello)    # Hello all

"""
Но стоит отметить, что импорт в глобальное пространство имен чреват коллизиями 
имен функций. Например, если у нас том же файле определена функция с тем же именем
до ее вызова, то будет вызываться функция, которая определена последней:
"""
from Module import *
  
print_message("Hello work")  # Message: Hello work - применяется функция из модуля message
 
def print_message(some_text):
    print(f"Text: {some_text}")
  
print_message("Hello work")  # Text: Hello work - применяется функция из текущего файла

# Установка псевдонимов
import Module as mes  # модуль message проецируется на псевдоним mes
 
# выводим значение переменной hello
print(mes.hello)        # Hello all
# обращаемся к функии print_message
mes.print_message("Hello work")  # Message: Hello work

from Module import print_message as display
from Module import hello as welcome
 
print(welcome)          # Hello all - переменная hello из модуля message
display("Hello work")   # Message: Hello work - функция print_message из модуля message

"""
Псевдонимы могут быть полезны, когда нас не устраивают имена функций и переменных, 
например, они слишком длинные, и мы хотим их сократить, либо мы хотим дать им более 
описательные, с нашей точки зрения, имена. Либо если в текущем файле уже есть 
функциональность с теми же именами, и с помощью установки псевдонимов мы можем 
избежать конфликта имен. Например:
"""
from Module import print_message as display
 
def print_message(some_text):
    print(f"Text: {some_text}")
 
# функция print_message из модуля message
display("Hello work")       # Message: Hello work
 
# функция print_message из текущего файла
print_message("Hello work")  # Text: Hello work

# Имя модуля
"""
При выполнении модуля среда определяет его имя и присваивает его глобальной 
переменной __name__ (с обеих сторон по два подчеркивания). Если модуль является 
запускаемым, то его имя равно __main__ (также по два подчеркивания с каждой стороны).
Если модуль используется в другом модуле, то в момент выполнения его имя аналогично 
названию файла без расширения py. И мы можем это использовать. Так, изменим 
содержимое модуля.
В данном случае в модуль message.py для тестирования функциональности модуля 
добавлена функция main. И мы можем сразу запустить файл message.py отдельно от 
всех и протестировать код.
"""
