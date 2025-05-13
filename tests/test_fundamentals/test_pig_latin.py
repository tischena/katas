from fundamentals.pig_latin import pig_latin_func

def test_consonant_ay():
    input = 'northcoders'
    output = 'orthcodersnay'
    assert pig_latin_func(input) == output
    
def test_consecutive_consonants_ay():
    input = 'sheffield'
    output = 'effieldshay'
    assert pig_latin_func(input) == output
    
def test_vowel_way():
    input = 'algorithm'
    output = 'algorithmway'
    assert pig_latin_func(input) == output
    
def test_sentence_mix():
    input = 'keep on coding'
    output = 'eepkay onway odingcay'
    assert pig_latin_func(input) == output