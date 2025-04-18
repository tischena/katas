from morse_decoder import morse_decoder_func

def test_one_letter_h():
    input = '....'
    output = 'H'
    assert morse_decoder_func(input) == output

def test_word_northcoders():
    input = '-. --- .-. - .... -.-. --- -.. . .-. ...'
    output = 'NORTHCODERS'
    assert morse_decoder_func(input) == output

def test_sentence():
    input = "--. --- --- -..   -- --- .-. -. .. -. --.   -. --- .-. - .... -.-. --- -.. . .-. ..."
    output = 'GOOD MORNING NORTHCODERS'
    assert morse_decoder_func(input) == output