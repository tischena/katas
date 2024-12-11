#import sys
#sys.path.append('../katas')

from task1 import replace_space, perfect_square, trailing_zeroes_fact

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