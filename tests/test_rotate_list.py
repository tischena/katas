from rotate_list import rotate_list_func

def test_zero_list_unchanged():
    input_list = [1, 2, 3]
    input_number = 0
    output = [1,2,3]
    assert rotate_list_func(input_list, input_number) == output

def test_positive_num_rotate_right():
    input_list = [1, 2, 3]
    input_number = 1
    output = [3,1,2]
    assert rotate_list_func(input_list, input_number) == output

def test_positive_nums_rotate_right():
    input_list = [1, 2, 3, 4, 5]
    input_number = 3
    output = [3,4,5,1,2]
    assert rotate_list_func(input_list, input_number) == output

def test_negative_num_rotate_left():
    input_list = [1, 2, 3]
    input_number = -1
    output = [2,3,1]
    assert rotate_list_func(input_list, input_number) == output

def test_negative_nums_rotate_left():
    input_list = [1,2,3,4,5]
    input_number = -3
    output = [4,5,1,2,3]
    assert rotate_list_func(input_list, input_number) == output