import time
import psutil

# We want to get the current amout of bytes that are sent
# and that are recieved in the past

last_recieved = psutil.net_io_counters().bytes_recv
last_sent = psutil.net_io_counters().bytes_sent
last_total = last_recieved + last_sent 

# this gives us hte current state. Wht is current state important because we 
# dont want to get total amout every time, like every tick

# We will be using the time module to get the update every 5/10/1 seconds

# 

while True:
    bytes_recieved = psutil.net_io_counters().bytes_recv
    bytes_sent = psutil.net_io_counters().bytes_sent
    bytes_total = bytes_recieved + bytes_sent

    new_recieved = bytes_recieved - last_recieved
    new_sent = bytes_sent - last_sent
    new_total = new_recieved + new_sent
    
    mb_new_recieved = new_recieved / 1024 / 1024 # originally recieved was in bytes
    mb_new_sent = new_sent / 1024 / 1024
    mb_new_total = mb_new_recieved + mb_new_sent

    print(f"{mb_new_recieved:.2f} Mb Recieved, {mb_new_sent:.2f} Mb Sent, {mb_new_total:.2f} Total")

    time.sleep(1)