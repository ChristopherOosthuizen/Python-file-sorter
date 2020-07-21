import os
import File
import threading


def sorted(name):
    f = File.File(name)
    f.setup()
    while True:
        if f.unsorted():
            f.sort()


for s in os.listdir():
    if os.path.splitext(s)[1] == '.sort':
        x = threading.Thread(target=sorted(s), args=(1,))
        x.start()
