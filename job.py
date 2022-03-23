from  datetime import datetime
from time import sleep
import requests

while True:
    body = {'lastping': datetime.now()}
    print(f'Sent: {body}')
    r = requests.post('http://127.0.0.1:5000/time', body)
    #print(f'Received: {r.json()}')
    print(f'Received: {r.text}')
    sleep(3)
