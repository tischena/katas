def pig_latin_func(our_input):
    our_input = our_input.split(' ')
    consecutive_consonants_list = ['sh', 'gl', 'ch', 'ph', 'tr', 'br', 'fr', 'bl', 'gr', 'st', 'sl', 'cl', 'pl', 'fl']
    vowels = 'euoai'
    return_output = ''
    for item in our_input:
        if item[0] in vowels:
            return_output += item + 'way'
        elif item[0:2] in consecutive_consonants_list:
            return_output += item[2::] + item[0:2] + 'ay'
        else:
            return_output += item[1::] + item[0] + 'ay'
        if len(our_input) > 1 and our_input.index(item) < (len(our_input) -1):
            return_output += ' '
    return return_output