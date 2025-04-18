def morse_decoder_func(morse_input):
    morse_letter_list = []
    result = ''
    if '   ' in morse_input:
        morse_word_list = morse_input.split('   ')
        for item in morse_word_list:
            morse_letter_lists = item.split(' ')
            morse_letter_list.append('   ')
            for letter_list in morse_letter_lists:
                morse_letter_list.append(letter_list)
        morse_letter_list = morse_letter_list[1::]
    elif ' ' in morse_input:
        morse_letter_list = morse_input.split(' ')
    else:
        morse_letter_list = morse_input
    morse_table = {
        ' ': '   ',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',   
        'T': '-', 
        'U': '..-',   
        'V': '...-', 
        'W': '.--',
        'X': '-..-', 
        'Y': '-.--',
        'Z': '--..',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.'
    }
    if '   ' in morse_input or ' ' in morse_input:
        for morse_letter in morse_letter_list:
            for key in morse_table:
                if morse_table[key] == morse_letter:
                    result += key
                else:
                    continue
    else:
        for key in morse_table:
                if morse_table[key] == morse_letter_list:
                    result += key
                else:
                    continue
    return result
