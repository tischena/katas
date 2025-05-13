#How can you replace string space with a given character

def replace_space(given_string, given_character):
    return given_string.replace(" ", given_character)

#Given a positive integer num, write a function that 
# returns True if num is a perfect square else False

import math
def perfect_square(given_num):
    if math.sqrt(given_num) % 1 == 0:
        return True
    return False

#Given an integer n, return the number 
# of trailing zeroes in n factorial n!

import math

def trailing_zeroes_fact(n):
    zero_count = 0
    factorial_number = str(math.factorial(n))
    zero_count = sum(1 for number in factorial_number[::-1] if number == '0')
    return zero_count

    # for digit in reversed(factorial_number):
    #     if digit == '0':
    #         zero_count += 1
    #     else:
    #         break
    # return zero_count



#You are provided with a large string and a 
# dictionary of the words. 
# You have to find if the input string 
# can be segmented into words using the dictionary or not.  

def string_to_dict(string_input, dict_input):
    if len(string_input) == 0:
        return True
    else:
        for i in range(1, len(string_input) + 1):
            if string_input[0:i] in dict_input:
                if string_to_dict(string_input[i:], dict_input):
                    return True
        return False
    
    
    
#Remove duplicates from a sorted array and get the length

def remove_dublicates(array_input):
    unique_array = []
    for num in array_input:
        if num not in unique_array:
            unique_array.append(num)
        else:
            continue
    return len(unique_array)



#Find the missing number in the array

def missing_num(array_input):
    sorted_array = sorted(array_input)
    if sorted_array[1] - sorted_array[0] == sorted_array[2] - sorted_array[1]:
        for i in range(len(sorted_array)):
            if sorted_array[i] + (sorted_array[1] - sorted_array[0]) not in array_input:
                return f'missing number is {sorted_array[i] + (sorted_array[1] - sorted_array[0])}'
    elif sorted_array[2] - sorted_array[1] == sorted_array[3] - sorted_array[2]:
        for i in range(len(sorted_array)):
            if sorted_array[i] + (sorted_array[2] - sorted_array[1]) not in array_input:
                return f'missing number is {sorted_array[i] + (sorted_array[2] - sorted_array[1])}'
    else:
        return 'no missing numbers'