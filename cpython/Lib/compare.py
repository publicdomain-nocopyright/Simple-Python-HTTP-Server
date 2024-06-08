def compare_last_positions(array, sequence):
    #_____________________________
    # Get the length of the sequence
    sequence_length = len(sequence)
    
    #_____________________________
    # Get the last positions of the array with the same length as the sequence
    array_end = array[-sequence_length:]
    
    #_____________________________
    # Compare the array end with the sequence
    return array_end == list(sequence)

#_____________________________
# Example usage
array = ['a', 'b', 'c', 'd', 'e']
sequence = 'cde'

result = compare_last_positions(array, sequence)
print(result)  # Output: True
