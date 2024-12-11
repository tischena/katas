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
