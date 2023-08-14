#!/usr/bin/python3

def multiple_returns(sentence):
    """This script returns the length of a string & its first (char)."""
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
