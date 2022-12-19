import json
import threading
import time
from datetime import datetime
import requests as requests
#https://api.coindesk.com/v1/bpi/currentprice.json

def bitcoinApi(URL):
    response = requests.get(URL).text
    response_info = json.loads(response)
    price = response_info['bpi']['USD']['rate_float']
    print(f"Aktualna cena Bitcoina: {price} USD")
    time.sleep(1)



def currentTime():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    time.sleep(10)


thread1 = threading.Thread(target=bitcoinApi("https://api.coindesk.com/v1/bpi/currentprice.json"))
thread2 = threading.Thread(target=currentTime())

thread1.start()
thread2.start()
