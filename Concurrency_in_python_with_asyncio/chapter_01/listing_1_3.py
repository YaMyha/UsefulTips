import threading
import time


def hello_from_thread():
    print(f'Hello from thread {threading.current_thread()}!')

hello_thread = threading.Thread(target=hello_from_thread) # create new thread for sync func hello_from_thread
hello_thread.start() # start created thread

total_threads = threading.active_count()
thread_name = threading.current_thread().name

print(f'Python is currently running {total_threads} thread(s)')
print(f'The current thread name is {thread_name}')

hello_thread.join() # make main thread wait for side thread finish

# Output here:
# Hello from thread <Thread(Thread-1 (hello_from_thread), started 26496)>!Python is currently running 2 thread(s)
#
# The current thread name is MainThread
# Because threads write to stdout concurrently and stdout doesn't have time to make line break so we have two \n in a row after merged Hello from thread <Thread(Thread-1 (hello_from_thread), started 1912)>!Python is currently running 2 thread(s)
# if we write
# def hello_from_thread():
#     time.sleep(1)
#     print(f'Hello from thread {threading.current_thread()}!')
# then output will be with correct line breaks because main thread would have finished its print already