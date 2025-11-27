import os
import threading

print(f'Python process running with process id: {os.getpid()}')

total_threads = threading.active_count() # get number of current threads
thread_name = threading.current_thread().name # get name of the current thread

print(f'Python is currently running {total_threads} thread(s)')
print(f'The current thread name is {thread_name}')