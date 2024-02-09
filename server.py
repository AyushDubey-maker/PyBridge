# import socket

# HOST = 'localhost'
# PORT = 12345

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect((HOST, PORT))
#     print("Connected to Java Server")
#     data = s.recv(1024)
#     print('Received from Java Server:', repr(data))


import json
import time
import os

# Initial delay
delay_seconds = 1

try:
    while True:
        if os.path.exists('data.json'):
            if os.path.getsize('data.json') > 0:  # Check if file is not empty
                with open('data.json') as json_file:
                    data = json.load(json_file)
                    if data:  # Check if there's any data in the JSON
                        delay_seconds = 60  # Change delay to 1 minute
                        for key, value in data.items():
                            print(key + ":", value)
                        print("Delay changed to 1 minute.")
        else:
            print("Waiting for data.json to be created...")
        time.sleep(delay_seconds)  # Adjust delay based on condition
finally:
    # Clear the contents of data.json if it's not empty
    if os.path.exists('data.json') and os.path.getsize('data.json') > 0:
        open('data.json', 'w').close()
        print("Cleared data.json")



