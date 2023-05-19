import pywhatkit
from datetime import datetime, timedelta
import time

def send_msg(no, time_now):

    current_time = time_now.strftime("%H:%M").split(':')
    name = no['name']
    pywhatkit.sendwhatmsg(no['number'],f"testing dari wa blast untuk: {name}",current_time[0],current_time[1])



if __name__=="__main__":
    data = [
        {
            "number": "+6281210693426",
            "name":"nuhinahinu"
        }
    ]
    for d in data: 
        send_msg(d,datetime.now() + timedelta(minutes=2))
        time.sleep(60)