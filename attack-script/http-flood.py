import requests
import time
import threading

url = 'http://localhost:8000'

def send_req():
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")

for i in range(5000):
    thread = threading.Thread(target=send_req)
    thread.start()
    time.sleep(0.02)
