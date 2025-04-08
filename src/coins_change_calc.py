def coins_change_calc_func(coins_amount):
    coins_dictionary = {
        '50' : 0,
        '20' : 0,
        '10' : 0,
        '5' : 0,
        '2' : 0,
        '1' : 0
    }
    while coins_amount != 0:
        if coins_amount>= 50:
            coins_amount -= 50
            coins_dictionary['50'] += 1
            coins_change_calc_func(coins_amount)
        elif coins_amount>= 20:
            coins_amount -= 20
            coins_dictionary['20'] += 1
            coins_change_calc_func(coins_amount)
        elif coins_amount>= 10:
            coins_amount -= 10
            coins_dictionary['10'] = coins_dictionary['10'] + 1
            coins_change_calc_func(coins_amount)
        elif coins_amount>= 5:
            coins_amount -= 5
            coins_dictionary['5'] += 1
            coins_change_calc_func(coins_amount)
        elif coins_amount>= 2:
            coins_amount -= 2
            coins_dictionary['2'] += 1
            coins_change_calc_func(coins_amount)
        else:
            coins_amount -= 1
            coins_dictionary['1'] += 1
            coins_change_calc_func(coins_amount)
        
    change_dict = {key: value for key, value in coins_dictionary.items() if value != 0}
    return change_dict