#!/usr/bin/python3

def multiple_returns(sentence):
    len_sentence = len(sentence)

    if len_sentence == 0:
        result = (0, None)
    _result = (len_sentence, sentence[0])
    return _result
