def find_common_words_count(first_string, second_string):
    first_list = first_string.split(' ')
    second_list = second_string.split(' ')

    first_set = set(first_list)
    second_set = set(second_list)

    common_words = set.intersection(first_set, second_set)
    return len(common_words)


phrase_1 = 'кот зол как лев дай мне сыр дай мне суп'
phrase_2 = 'кто ест сыр тот кот кто ест суп тот нет'

common_words_count = find_common_words_count(phrase_1, phrase_2)
print('Общих уникальных слов в предложениях:', common_words_count)
