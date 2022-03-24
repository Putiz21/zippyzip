import tarfile
import time
import os
from os import listdir

while True:
    time.sleep(0.05)
    for file in listdir('/home/putiz/Pulpit/Unpack'):
        if not file == "unpacker.py":
            tar = tarfile.open(file)
            tar.extractall()
            tar.close()
            os.remove(file)
            pass