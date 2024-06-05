import threading
import time

def start_thread(function_name):
    thread = threading.Thread(target=function_name)
    thread.daemon = True
    thread.start()
    return thread

# Function to keep the thread alive
def wait_for_exit():
    while True:
        if input("Type 'exit' to quit: ").lower() == 'exit':
            print("Exiting...")
            break

# Function to print "test" every second
def print_test_every_second():
    while True:
        print("test")
        time.sleep(1)

# Create and start the threads
exit_thread = start_thread(wait_for_exit)
print_thread = start_thread(print_test_every_second)

# Main thread can continue to do other things if needed
try:
    while exit_thread.is_alive():
        # Perform other tasks here, if necessary
        exit_thread.join(1)  # Join with a timeout to keep the loop running
except KeyboardInterrupt:
    print("Received CTRL+C, exiting...")
    exit_thread.join()  # Ensure the exit_thread completes before exiting
