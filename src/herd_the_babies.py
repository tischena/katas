def herd_the_babies_func(letter_mix):
    letter_mix_list_sorted = sorted(list(letter_mix), key=lambda c: (c.lower(), c.islower()))
    sorted_letters = ''
    for item in letter_mix_list_sorted:
        sorted_letters += item
    return sorted_letters