def to_camel_case_func(sentence, bool):
    sentence = sentence.split(' ')
    return_sentence = ''
    if bool == True:
        for item in sentence:
            return_sentence += item.capitalize()
    else:
        for item in sentence:
            if item == sentence[0]:
                return_sentence += item
            else:
                return_sentence += item.capitalize()
        
    return return_sentence