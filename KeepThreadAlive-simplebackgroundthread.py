import threading
import time

# Define the function that will run in a separate thread
def function_name():
    while True:
        print("Thread is started")
        time.sleep(1)

# Start the thread
threading.Thread(target=function_name, daemon=True).start()

# Main program continues to run
def check_thread_alive():
    while True:
        time.sleep(1)
        # Check if the thread is alive
        for thread in threading.enumerate():
            if thread.name == 'Thread-1':  # Default name for the first thread
                print("Thread is alive")
                break
        else:
            print("Thread is not alive")
            break

# Start a separate thread to check if the original thread is alive
threading.Thread(target=check_thread_alive, daemon=True).start()

print("Main program is running")
time.sleep(5)
print("Main program is done")
