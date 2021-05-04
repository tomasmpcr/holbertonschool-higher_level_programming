#!/usr/bin/python3
def multiple_returns(sentence):
    ret = (len(sentence), None)
    if sentence:
        ret = (len(sentence), sentence[0])
    return (ret)
