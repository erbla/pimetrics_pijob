import datetime
import time
import requests
import psutil

while True:
    body = {
        'lastping': datetime.datetime.now(),
        'cpu-usage': psutil.cpu_percent(),
        'ram-usage': psutil.virtual_memory().percent,
        'disk-usage': psutil.disk_usage('/').percent,
        }
    print(f'Sent: {body}')
    try:
        r = requests.post('http://localhost:5000/update', body)
        print(f'Received: {r.text}')
    except:
        print(f'Error sending request to server')
    time.sleep(5)
