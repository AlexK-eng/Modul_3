# This is a Task 3_5.

def get_multiplied_digits(number):
    # if type(number) != int: return print(f'Введите целое число, а не {type(number)}')
    number = int(number)
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number[1:]) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


print(get_multiplied_digits('00203'))
