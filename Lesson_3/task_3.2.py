# Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать
# параметры как именованные аргументы. Реализовать вывод
# данных о пользователе одной строкой.

def my_func(name, soname, bdate, tnumber, lcity, email,):
    return f'имя: {name}, фамилия: {soname}, год_рождения: {bdate}, телефон: {tnumber}, город_проживания: {lcity},' \
           f'почта: {email}'


name =input('Имя: ')
soname =input('Фамилия: ')
bdate =input('Дата рождения:')
tnumber =input('номер телефона:')
lcity =input('город проживания: ')
email =input('Почта: ')

print(my_func(name=name, soname='soname', bdate=bdate, tnumber=tnumber,
        lcity='lcity', email='email'))
