import datetime
import time
import requests

while True:
    body = {'lastping': datetime.datetime.now()}
    print(f'Sent: {body}')
    try:
        r = requests.post('http://localhost:5000/time', body)
    except:
        print(f'Error sending request to server')
    print(f'Received: {r.text}')
    time.sleep(3)
