import datetime
import time
import requests

while True:
    body = {'lastping': datetime.datetime.now()}
    print(f'Sent: {body}')
    r = requests.post('http://localhost:5000/time', body)
    #print(f'Received: {r.json()}')
    print(f'Received: {r.text}')
    time.sleep(3)
