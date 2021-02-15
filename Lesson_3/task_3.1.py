# Реализовать функцию, принимающую два
# числа(позиционные аргументы) и выполняющую их
# деление.Числа запрашивать у пользователя, предусмотреть
# обработку ситуации деления на ноль.

def my_func (x, y):
    try:
        z = x / y
        return z
    except ZeroDivisionError:
        return 'y не должеть быть 0'
    except ValueError:
        return ' введите только число'
print(my_func(int(input('Ввкдите x =')), int(input('Введите y ='))))