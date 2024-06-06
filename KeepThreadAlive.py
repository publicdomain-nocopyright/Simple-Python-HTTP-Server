import time

#__________________________________________________________________
# Function to keep the thread alive
def wait_for_exit():
    try:
        while True:
            if input(f" {threading.current_thread().name} Type 'exit' to quit:").lower() == 'exit':
                print("Exiting...")
                break
    except:
        pass
# Function to print "test" every second
def print_test_every_second():
    while True:
        print(f"Running in thread: {threading.current_thread().name}")
        time.sleep(1)

import threading
def BackgroundThread(**configs):
    thread = threading.Thread(**configs, daemon = True)
    thread.start()
    return thread

#__________________________________________________________________

# Create and start the threads
exit_thread = BackgroundThread(target=wait_for_exit)
print_thread = BackgroundThread(target=print_test_every_second)

# Main thread can continue to do other things if needed
try:
    while exit_thread.is_alive():
        exit_thread.join(1)  # Join with a timeout to keep the loop running
except KeyboardInterrupt:
    print("Received CTRL+C, exiting...")

