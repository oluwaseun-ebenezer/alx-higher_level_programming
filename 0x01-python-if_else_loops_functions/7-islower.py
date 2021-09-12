#!/usr/bin/python3
def islower(char):
    '''
    CHecks whether charcater passed to it is lowercase or uppercase
    '''
    if ord(char) >= 97 and ord(char) <= 122:
        return True
    return False
