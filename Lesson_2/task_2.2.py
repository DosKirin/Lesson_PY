insert = int(input('Введите кол-во элементов'))
my_lst =[]
i = 0
el = 0
while i < insert:
    my_lst.append(input('Введите следующее значение из списка '))
    i += 1

for el in range(int(len(my_lst)/2)):
    my_lst[el], my_lst[el + 1] = my_lst [el + 1], my_lst[el]
    el += 2
print(my_lst)
