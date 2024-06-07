#_____________________________
# Import the msvcrt module
import msvcrt

#_____________________________
# Function to read characters without pressing enter
def read_chars():
    print("Press 'q' to exit.")
    while True:
        if msvcrt.kbhit():
            char = msvcrt.getch().decode('utf-8')
            if char == 'q':
                break
            print(f'You pressed: {char}')

#_____________________________
# Call the function
read_chars()
