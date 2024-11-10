my_string = input("Введите строку: ")
print(f'Кол-во символов в строке: {len(my_string)}')
print(f'Верхний регистр: {my_string.upper()}')
print(f'Нижний регистр: {my_string.lower()}')
no_spaces_string = my_string.replace('','')
print(f'Без пробелов:{no_spaces_string}')
print(f'Первый символ: {my_string[0]}')
print(f'Последний символ: {my_string[-1]}')
per = 'Hello,'
per2 = 'Urban'
print(per, per2, sep='')