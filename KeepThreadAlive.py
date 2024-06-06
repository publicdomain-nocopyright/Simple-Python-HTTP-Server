import threading
import time

def newBackgroundThread(function_name):
    thread = threading.Thread(target=function_name, daemon = True)
    thread.start()
    return thread

# Function to keep the thread alive
def wait_for_exit():
    try:
        while True:
            print(f"Running in thread: {threading.current_thread().name}")
            if input("Type 'exit' to quit: \n").lower() == 'exit':
                print("Exiting...")
                break
    except:
        pass
# Function to print "test" every second
def print_test_every_second():
    while True:
        print(f"Running in thread: {threading.current_thread().name}")
        print("test")
        time.sleep(1)

# Create and start the threads
exit_thread = newBackgroundThread(wait_for_exit)
print_thread = newBackgroundThread(print_test_every_second)

# Main thread can continue to do other things if needed
try:
    while exit_thread.is_alive():
        exit_thread.join(1)  # Join with a timeout to keep the loop running
except KeyboardInterrupt:
    print("Received CTRL+C, exiting...")

