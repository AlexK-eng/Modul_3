# This is a Task 3_1.

calls = 0

def count_calls():
    # Счетчик вызова функций.
    global calls
    calls += 1

def string_info(string):
    str_tuple = (len(string), string.upper(), string.lower())
    count_calls()
    return str_tuple

def is_contains(string, _list):
    count_calls()
    string = string.upper()
    str_list = ' '
    convert_list = str_list.join(_list)
    convert_list = convert_list.upper()
    up_list = convert_list.split()
    if up_list.count(string) > 0:
        return True
    return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)


