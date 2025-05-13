from fundamentals.fold_string import fold_string_func

def test_code_even():
    input = 'code'
    output = 'oced'
    assert fold_string_func(input) == output 

def test_abcdef_even():
    input = 'abcdef'
    output = 'cbafed'
    assert fold_string_func(input) == output

def test_python_even():
    input = 'python'
    output = 'typnoh'
    assert fold_string_func(input) == output

def test_Northcoders_odd():
    input = 'Northcoders'
    output = 'htroNcsredo'
    assert fold_string_func(input) == output

def test_sentence():
    input = 'python is cool'
    output = 'typnoh is oclo'
    assert fold_string_func(input) == output