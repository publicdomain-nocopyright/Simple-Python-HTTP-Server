import threading
def BackgroundThread(**configs):
    thread = threading.Thread(**configs, daemon = True)
    thread.start()
    return thread