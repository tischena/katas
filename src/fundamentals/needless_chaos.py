import random

results_array = [] # global so it can store results

def needless_chaos_func(num1, num2):
    
    result = num1 - num2
    results_array.append(result)
    random_number_from_list = random.choice(results_array)
    return random_number_from_list