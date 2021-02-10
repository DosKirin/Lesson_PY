#  Создать текстовый файл (не программно), сохранить в нем
# несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

file_name = '/Users/matvey/Desktop/Lessons_1/Lesson_5/My_file2.txt'

with open(file_name, 'r') as my_file:
    lines = my_file.readlines()
with open(file_name, 'r') as my_file:
    for index, value in enumerate (lines):
        num_words = len(value.split())
        my_file.read(.format(index + 1, num_words))







#     count = sum(1 for line in my_file)
#     count = 0
# with open(file_name, 'r') as my_file:
#     for line in my_file:
#         count += 1
# print(count)
# print(f'Колличетсво строк: {len(lines)}')
# for i, line in enumerate(lines,1):
#     print(f'колличетсво слов в {i} строке: {len(line.split())}')
