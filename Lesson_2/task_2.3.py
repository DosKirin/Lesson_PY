seasons_list = int(input('Введите номер месяца'))
if seasons_list <= 12 and seasons_list >=1:
    month_dict = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель',
                 5: 'Май', 6: 'Июнь', 7: 'Июль', 8: 'Август', 9: 'Сентябрь',
                 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}
    month_list = list(month_dict.values())
    for i, el in enumerate(month_list):
        if i == seasons_list-1:
            print(f'Номер месяца is {month_list[i]}')
            break
    print(f'Название месяца is {month_dict[seasons_list]}')
else:
    print('Ошибка')



