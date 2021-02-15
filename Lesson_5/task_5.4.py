# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

r_filename = '/Users/matvey/Desktop/Lessons_1/Lesson_5/T_r4.txt'
w_filename = '/Users/matvey/Desktop/Lessons_1/Lesson_5/t_w4.txt'
rus_tags = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_tags = [ ]
with open(r_filename, 'r') as my_file:
    # lines = my_file.readlines()
    for i in my_file:
        i = i.split(' ', 1)
        new_tags.append((rus_tags[i[0]] + ' ' + i[1]))
    print(new_tags)

with open(w_filename, 'w') as my_file:
    my_file.writelines(new_tags)



