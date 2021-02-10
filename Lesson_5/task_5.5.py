# Создать (программно) текстовый файл, записать в него
# программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


num_tags = "11 177.2 561 77.6 90"

summ = 0

try:
    with open ('Task_5', 'w' ) as my_file:
        my_file.write(num_tags)

    with open ('Task_5', 'r') as my_file:
        data = my_file.read()

    for item in data.split ():
        summ += float (item)
except IOError as e:
    print (e)
except ValueError:
    print ("Неконсистентные данные")

print ({summ},)
