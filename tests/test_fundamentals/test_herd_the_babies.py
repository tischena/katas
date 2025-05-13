from fundamentals.herd_the_babies import herd_the_babies_func

def test_aA_return_Aa():
    input = 'aA'
    output = 'Aa'
    assert herd_the_babies_func(input) == output

def test_aBA_return_AaB():
    input = 'aBA'
    output = 'AaB'
    assert herd_the_babies_func(input) == output

def test_bbaBccAC_return_AaBbbCcc():
    input = 'bbaBccAC'
    output = 'AaBbbCcc'
    assert herd_the_babies_func(input) == output
    
def test_AaBbbBaAbAbbAbB_return_AAAAaaBBBbbbbbb():
    input = 'AaBbbBaAbAbbAbB'
    output = 'AAAAaaBBBbbbbbb'
    assert herd_the_babies_func(input) == output