#import sys
#sys.path.append('../katas')

from task1 import replace_space, perfect_square, trailing_zeroes_fact, string_to_dict, remove_dublicates, missing_num

def test_replace_space():
    input1 = 'D t C mpBl ckFrid yS le'
    input2 = 'a'
    output = 'DataCampBlackFridaySale'
    assert replace_space(input1, input2) == output
    
    
    
def test_perfect_square_of_36():
    input = 36
    output = True
    assert perfect_square(input) == output
    
def test_perfect_square_of_10():
    input = 10
    output = False
    assert perfect_square(input) == output
    


def test_trailing_zeroes_fact():
    input = 10 #3628800
    output = 2
    assert trailing_zeroes_fact(input) == output
    
    
    
def test_string_to_dict_true():
    input = 'datacamp'
    dict_string = [ 
        'cam', 
        'camp', 
        'lack',
        'data'
    ]
    output = True
    assert string_to_dict(input, dict_string) == output
    
def test_string_to_dict_false():
    input = 'datacamps'
    dict_string = [ 
        'cam', 
        'camp', 
        'lack',
        'data'
    ]
    output = False
    assert string_to_dict(input, dict_string) == output
    


def test_remove_dublicates():
    input = [1,2,2,3,2,5]
    output = 4
    assert remove_dublicates(input) == output
    
    
    
def test_missing_num():
    input = [1,5,6,3,4]
    output = 'missing number is 2'
    assert missing_num(input) == output