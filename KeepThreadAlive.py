import threading

def start_thread(function_name):
    thread = threading.Thread(target=function_name)
    thread.daemon = True
    thread.start()

# Function to keep the thread alive
def wait_for_exit():
    while True:
        if input("Type 'exit' to quit: ").lower() == 'exit':
            print("Exiting...")
            break

# Create and start the thread
exit_thread = threading.Thread(target=wait_for_exit)
exit_thread.start()

# Main thread can continue to do other things if needed
try:
    while exit_thread.is_alive():
        # Perform other tasks here, if necessary
        exit_thread.join(1)  # Join with a timeout to keep the loop running
except KeyboardInterrupt:
    print("Received CTRL+C, exiting...")
    exit_thread.join()  # Ensure the exit_thread completes before exiting
