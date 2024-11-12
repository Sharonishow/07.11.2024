my_dict = {'Nikita': 2003, 'Roma': 2002, 'Artem': 2009}
a = my_dict.pop('Roma')
print(my_dict)
my_dict.update({'Mira': 1999, 'Muza': 2015})
print(my_dict.get('Sanya'))
print(my_dict['Artem'])
print(my_dict)
print(a)

my_set = {1, 1, 1, 'Звезда', 'Звезда', 4343.34324}
print(my_set)
b = my_set.remove('Звезда')
print(my_set)
my_set.update((2, 2, 2, 4, 4, 1.5))
print(my_set)

