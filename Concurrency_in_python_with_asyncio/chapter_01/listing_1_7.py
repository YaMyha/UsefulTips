# Sync making requests to server

import time
import requests

def read_example() -> None:
    response = requests.get('http://example.com/')
    print(response.status_code)

sync_start = time.time()

read_example()
read_example()

sync_end = time.time()

print(f'Running time: {sync_end - sync_start:.4f} seconds')
# Output
# 200
# 200
# Running time: 0.8116 seconds

