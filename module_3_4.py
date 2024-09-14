# This is a Task 3_1.
def single_root_words(root_word, *other_words):
    same_words = [*other_words]
    return [same_words[x] for x in range(len(same_words)) if
                  ((root_word.upper()) in (same_words[x].upper()) or
                   (same_words[x].upper()) in (root_word.upper()))]


result1 = single_root_words('rich', 'richiest',
                            'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable',
                            'Disable', 'Bagel')
print(result1)  # ['richiest', 'orichalcum', 'richies']
print(result2)  # ['Able', 'Disable']
