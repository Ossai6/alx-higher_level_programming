#!/usr/bin/python3

def multiple_returns(sentence):
    len_sentence = len(sentence)

    if len_sentence == 0:
        result = (0, None)
    else:
        _result = (len_sentence, sentence[0:1])
        return _result
