def till_addition_func(till_dict):
    till_sum = 0
    for key in till_dict:
        if key[-1] == 'p':
            till_sum += ((int(key[:-1])) * till_dict[key] ) / 100
        else:
            till_sum += (int(key[1:])) * till_dict[key]
            
    return f'£{till_sum}'
    
    