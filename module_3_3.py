# Задача "Распаковка"
def print_params(a=1, b='string', c=True):
    print(a, b, c)


# Параметры по умолчанию:
print_params()  # 1 string True
print_params(b=25)  # 1 25 True
print_params(c=[1, 2, 3])  # 1 string [1, 2, 3]

# Распаковка параметров:
values_list = [1, True, 'String']
values_dict = {'a': 6, 'b': 'strong', "c": False}
print_params(*values_list)
print_params(**values_dict)

# Распаковка + отдельные параметры:
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)
