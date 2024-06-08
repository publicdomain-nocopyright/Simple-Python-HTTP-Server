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

def readkeyuntil(text, keys):
    while True:
        # Read key input and append to keys list
        keys.append(readkey())
        print(keys)
        
        # Compare keys with text in reverse order
        if len(keys) >= len(text):
            if keys[-len(text):] == list(text):
                print("Matched text:", text)
                return

##_____________________________
## Example usage
readkeyuntil("waffle", [])
