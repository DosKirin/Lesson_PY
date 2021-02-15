# Создать текстовый файл (не программно), построчно записать фамилии сотрудников
 # и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
 # вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

file_name = '/Users/matvey/Desktop/Lessons_1/Lesson_5/employers.txt'


with open (file_name, 'r' ) as my_file:
    employees = my_file.readlines()
    workers = { }
    for line in my_file:
        key, value = line.split ('n|')
        workers[key] = value
        if int (value) < 20000:
            print ( f'{key}: зарплата меньше 20000' )

