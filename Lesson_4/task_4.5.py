# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce()


from functools import reduce
my_list = [el for el in range(99,1001) if el % 2 == 0]
def my_func(arg1,arg2):
    return arg1 * arg2

print(reduce(my_func, my_list))


# from functools import reduce
# my_list = [el for el in range(99,1001) if el % 2 == 0]
#
#
# print(reduce(my_list))
#
# я сначала сделал так появилась ошибка
#     print(reduce(my_list))
# TypeError: reduce expected at least 2 arguments, got 1
# я правильно понял что редус нужен был 2й аргумент? и добавил через функцию используя значения аргс
# прости я сложно выражаю мысль
# как решаешь ты я не понял не нашел в методичке operator