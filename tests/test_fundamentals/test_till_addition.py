from fundamentals.till_addition import till_addition_func

def test_ads_ps():
    input = { "1p": 1, "2p": 1, '10p': 1 }
    output = "£0.13"
    assert till_addition_func(input) == output
    
def test_ads_ps_and_pounds_singular():
    input = { "1p": 1, "2p": 1, '10p': 1, '£5': 1 }
    output = "£5.13"
    assert till_addition_func(input) == output

def test_ads_ps_and_pounds_multiple():
    input = { "1p": 1, "2p": 2, '10p': 1, '£5': 4 }
    output = "£20.15"
    assert till_addition_func(input) == output

