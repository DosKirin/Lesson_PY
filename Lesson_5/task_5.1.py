


with open('My_file.txt', 'w') as my_file:
    my_text = input('введите текс для записи\n')
    while my_text:
        my_file.writelines(my_text)
        my_text = input('Введите текст для записи\n')
        if not my_text:
            break

with open('My_file.txt', 'r') as my_file:
    while True:
        conte = my_file.read()
        print(conte)
        if not conte:
            break
