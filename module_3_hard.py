def calculate_structure_sum(data_structure):
    global flat_sum
    for i in data_structure:
        if isinstance(i, int):
            flat_sum += i
        elif isinstance(i, str):
            flat_sum += len(i)
        elif isinstance(i, list):
            calculate_structure_sum(i)
        elif isinstance(i, dict):
            calculate_structure_sum([element for pair in
                                     i.items() for element in pair])
        elif isinstance(i, tuple):
            calculate_structure_sum(list(i))
        elif isinstance(i, set):
            calculate_structure_sum(list(i))
    return flat_sum


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
flat_sum = 0
print(calculate_structure_sum(data_structure))
