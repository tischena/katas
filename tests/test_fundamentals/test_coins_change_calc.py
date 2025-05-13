from fundamentals.coins_change_calc import coins_change_calc_func

def test_one_p_singular():
    input = 1
    output = {'1':1}
    assert coins_change_calc_func(input) == output

def singular():
    input = 2
    output = {'2' : 1}
    assert coins_change_calc_func(input) == output

def test_multiple():
    input = 7
    output = {'5':1,'2':1}
    assert coins_change_calc_func(input) == output

def test_multiple():
    input = 13
    output = {'10':1,'2':1,'1':1}
    assert coins_change_calc_func(input) == output

def test_double_multiple():
    input = 45
    output = {'20':2,'5':1}
    assert coins_change_calc_func(input) == output
