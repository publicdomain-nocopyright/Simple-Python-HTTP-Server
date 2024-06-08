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

global_array = []
#_____________________________________
def add_argument_to_global_array(func):
    def wrapper(*args):
        global global_array
        if args[0] not in global_array:  # Avoid duplicates
            global_array.append(args[0])
        return func(*args)
    return wrapper

@add_argument_to_global_array
def reversearray_charmatch(text, array):
    global reversearray_charmatch_result
    if len(array) >= len(text):
        if array[-len(text):] == list(text):
            reversearray_charmatch_result = text
            return True
    return False

def getreversearrayinput():
    input_keys = []
    while True:
        last_input_key = readkey()
        input_keys += last_input_key
        print(input_keys)
        if last_input_key == '\r':
            return input_keys
        
def arraytostring(array):
    result = ""
    for letter in array:
        result += letter + ""
    return result


# TODO: While typing, give a choice or parameter to type in. The "ok " (and space) could be used to clear the input. 
# TODO: Maybe a double space (  ) would be great for clearing the input. TAB key also could be great.
# All this might be great for Command Line interface, but maybe not for Scripting Language.
import sys
import webbrowser
import os
def readkeyuntil(text, keys):
    while True:
        # Read key input and append to keys list
        lastkey = readkey()
        print(lastkey, end="", flush=True)
        keys.append(lastkey)
       
        if lastkey == '\t' or lastkey == '\r':
            print("\r                                                \r", end="", flush=True)
        #print(arraytostring(keys))
        
        # TOOD: Should be executed once at the beginning of the program.
        if reversearray_charmatch("credits", keys):
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')
            print("Matched text:", reversearray_charmatch_result)
            print("Public Domain Laboratories.")

        if reversearray_charmatch(text, keys):
            print("Matched text:", text)
        if reversearray_charmatch("fooo", keys):
            print("Matched text:", reversearray_charmatch_result)
        if reversearray_charmatch("waffle store", keys):
            webbrowser.open("https://www.example.com")
        if reversearray_charmatch("open github", keys):
            webbrowser.open("https://www.github.com")
        if reversearray_charmatch("youtube", keys):
            webbrowser.open("https://www.youtube.com")
        if reversearray_charmatch("revolt", keys):
            webbrowser.open("https://app.revolt.chat/server/")
        if reversearray_charmatch("about", keys):
            webbrowser.open("https://github.com/publicdomain-nocopyright/Simple-Python-HTTP-Server")
        if reversearray_charmatch("create file", keys):
            print("input start")
            stringarray = getreversearrayinput()
            stringarray.pop()
            input = arraytostring(stringarray)
            print(input)
            print("input end")
            open(input, 'w').close()
        if reversearray_charmatch("create folder", keys):
            print(" input start")
            stringarray = getreversearrayinput()
            stringarray.pop()
            input = arraytostring(stringarray)
            print(input)
            print("input end")
            os.makedirs(input, exist_ok=True)
        if reversearray_charmatch("input", keys):
            print("input start")
            input = arraytostring(getreversearrayinput())
            print(input)
            print("input end")
        if reversearray_charmatch("help", keys):
            print("\r                                                \r", end="", flush=True)
            print("Matched text:", reversearray_charmatch_result)
            print(global_array)
        if reversearray_charmatch("clear", keys):
            print("Matched text:", reversearray_charmatch_result)
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')
            print("Public Domain Laboratories.")
            print("Write \"help\" to get more information.")

        if reversearray_charmatch('computer', keys):
            print()
            import platform
            import psutil
            print(platform.system())
            print(platform.machine())
            print(platform.processor())
            print(round(psutil.virtual_memory().total / (1024**3), 2))

        if reversearray_charmatch("\x00k", keys):
            print("Matched text:", reversearray_charmatch_result)
            sys.exit()
        if reversearray_charmatch("exit", keys):
            print("Matched text:", reversearray_charmatch_result)
            sys.exit()
        if reversearray_charmatch('\x1b', keys):
            print("Matched text:", 'ESC')
            sys.exit()
        if reversearray_charmatch('\x03', keys):
            print("Matched text:", 'CTRL+C')
            sys.exit()
            

##_____________________________
## Example usage

try:
    print("Public Domain Laboratories.")
    print("Write \"help\" to get more information.")
    readkeyuntil("waffle", [])
except Exception as e:
    print(f"An error occurred: {e}")
    input("\nPress Enter to close the window...")

    