from fundamentals.sentence_to_camel_case import to_camel_case_func

def test_true():
    input1 = "this sentence"
    input2 = True
    output = "ThisSentence"
    assert to_camel_case_func(input1, input2) == output

def test_false():
    input1 = "this sentence"
    input2 = False
    output = "thisSentence"
    assert to_camel_case_func(input1, input2) == output

def test_bigger_sentence_mix():
    input1 = "This Bigger strange Sentence"
    input2 = True
    output = "ThisBiggerStrangeSentence"
    assert to_camel_case_func(input1, input2) == output
