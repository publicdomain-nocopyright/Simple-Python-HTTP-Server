# https://github.com/python/cpython/blob/main/Python/bltinmodule.c#L2136
# https://github.com/python/cpython/tree/main/Lib

import msvcrt

def readkey():
    return msvcrt.getwch()

# First version and concise
# def readkeyuntil(text, keys):
#     while list(text) != keys:
#         keys.append(readkey())
#         print(keys)
# 

# Second version and more handling support
def readkeyuntil(text, keys):
    while True:
        if list(text) != keys:
            keys.append(readkey())
            print(keys)
        else:  
            return

readkeyuntil("waffle", [])