#!/usr/bin/python3
#8multiple_returns

def multiple_returns(sentence):
    if len(sentence) == 0:
        first_letter = None
    else:
        first_letter = sentence[0]
    return len(sentence), first_letter
