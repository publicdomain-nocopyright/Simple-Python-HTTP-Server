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
#def readkeyuntil(text, keys):
#    while True:
#        if list(text) != keys:
#            keys.append(readkey())
#            print(keys)
#        else:  
#            return
        
# you can try to reverse the input string and match against array in reverse.
# Compare each letter of text from the end of keys array in reverse order, if it matches all text letters do a print().

#def compare_last_positions(arrays, sequence):
#    #_____________________________
#    # Get the length of the sequence
#    sequence_length = len(sequence)
#    #_____________________________
#    # Get the last positions of the array with the same length as the sequence
#    array_end = arrays[-sequence_length:]
#    print("-----")
#    print(array_end)
#    print(sequence)
#    #_____________________________
#    # Compare the array end with the sequence
#    return array_end == sequence
#
#def readkeyuntil(text, keys):
#    #_____________________________
#    # Function to simulate reading a key from the user
#    def readkey():
#        import msvcrt
#        return msvcrt.getch().decode()
#
#    while True:
#        #_____________________________
#        # Convert the text to a list of characters
#        text_list = list(text)
#        
#        #_____________________________
#        # Compare the last positions of the text with the keys
#        if not compare_last_positions(text_list, keys):
#            #_____________________________
#            # Append the read key to the keys list
#            key = readkey()
#            keys.append(key)
#            print(keys)
#        else:
#            #_____________________________
#            # Break the loop when the keys match the end of the text
#            return
#
###### Didn't work out as it compares whole array against array and not text letters in reverse order against key presses.

# Compare keys with text in reverse order

def reversearray_charmatch(text, array):
    global reversearray_charmatch_result
    if len(array) >= len(text):
        if array[-len(text):] == list(text):
            reversearray_charmatch_result = text
            return True
    return False


def readkeyuntil(text, keys):
    while True:
        # Read key input and append to keys list
        keys.append(readkey())
        print(keys)
        if reversearray_charmatch(text, keys):
            print("Matched text:", text)
        if reversearray_charmatch("fooo", keys):
            print("Matched text:", reversearray_charmatch_result)
        if reversearray_charmatch("waffle store", keys):
            print("Matched text:", "waffle store")
            import webbrowser
            webbrowser.open("https://www.example.com")
        if reversearray_charmatch("open github", keys):
            print("Matched text:", "open github")
            import webbrowser
            webbrowser.open("https://www.github.com")
        if reversearray_charmatch("exit", keys):
            print("Matched text:", "exit")
        if reversearray_charmatch('\x1b', keys):
            print("Matched text:", 'ESC')
            import sys
            sys.exit()
        if reversearray_charmatch('\x03', keys):
            print("Matched text:", 'CTRL+C')
            import sys
            sys.exit()
            

##_____________________________
## Example usage
readkeyuntil("waffle", [])
