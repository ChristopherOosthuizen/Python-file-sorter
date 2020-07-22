import os
import File
import threading
import time

def sorted(name):
    f = File.File(name)
    f.setup()
    while True:
        if f.unsorted():
            f.sort()
        time.sleep(5)


for s in os.listdir("sorts"):
    if os.path.splitext(s)[1] == '.sort':
        x = threading.Thread(target=sorted(s), args=(1,))
        x.daemon = True
        x.start()
