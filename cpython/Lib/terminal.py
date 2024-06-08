# https://github.com/python/cpython/blob/main/Python/bltinmodule.c#L2136
# https://github.com/python/cpython/tree/main/Lib

import msvcrt

def readkey():
    return msvcrt.getwch()

def readkeyuntil(text, keys):
    while list(text) != keys:
        keys.append(readkey())
        print(str(keys))

readkeyuntil("waffle", [])