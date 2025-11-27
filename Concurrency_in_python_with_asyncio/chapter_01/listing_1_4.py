import multiprocessing
import os

def hello_from_process():
    print(f'Hello from child process {os.getpid()}')

if __name__ == '__main__':
    hello_process = multiprocessing.Process(target=hello_from_process) # create child process
    hello_process.start() # start child

    print(f'Hello from parent process {os.getpid()}')

    hello_process.join() # wait for child process in main process

# Output
# Hello from parent process 25912
# Hello from child process 24376
# Main prints first because processor needs some time to create child process