# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
def my_func(a, b , c):
    seq = [a, b, c]
    total =[]
    max_1 = max(seq)
    total.append(max_1)
    seq.remove(max_1)
    max_2 = max(seq)
    total.append(max_2)
    print(sum(total))
my_func(-10, 20, 94)


