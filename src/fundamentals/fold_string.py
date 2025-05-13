def fold_string_func(input_string):
    input_string = input_string.split(' ')
    result = ''
    for input_strings in input_string:
        if len(input_strings) % 2 == 0: #even
            first_half = input_strings[:len(input_strings)//2]
            second_half = input_strings[-(len(input_strings)//2):]
            result += first_half[::-1] + second_half[::-1]    
        else: #odd
            first_half = input_strings[:len(input_strings)//2]
            second_half = input_strings[-(len(input_strings)//2):]
            middle = input_strings[len(input_strings)//2]
            result += first_half[::-1] + middle + second_half[::-1]
            
        if len(input_string) > 1 and input_string.index(input_strings) < (len(input_string) -1):
            result += ' '
        else:
            continue
    return result