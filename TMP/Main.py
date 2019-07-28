import ptvsd
import datetime
import time

host = "127.0.0.1"
port = 5678
print("Waiting for debugger attach at %s:%s ......" % (host, port))
ptvsd.enable_attach(address=(host, port))
ptvsd.wait_for_attach()


while True:
    time.sleep(1)
    cur_data = datetime.datetime.now()
    print(cur_data)
