# Making requests to server in multiple threads

import time
import threading
import requests

def read_example() -> None:
    response = requests.get('http://example.com/')
    print(response.status_code)

thread_1 = threading.Thread(target=read_example)
thread_2 = threading.Thread(target=read_example)

thread_start = time.time()

thread_1.start()
thread_2.start()

print('All threads running!')

thread_1.join()
thread_2.join()

thread_end = time.time()
print(f'Total time: {thread_end - thread_start:.4f} seconds')
# Output
# All threads running!
# 200
# 200
# Total time: 0.4015 seconds
# Comparing to sync 0.8116 it's 2 times less!
# The gain in speed is achieved due to 2 threads. The process can turn threads for IO bound operations, so when 1st thread is waiting for response from server the process turns on 2nd thread and sends 2nd request
# Even if requests is sync library multiple threads allows to use idle time for work