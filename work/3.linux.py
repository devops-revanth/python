#!/usr/bin/env python3

import os
import time

for log in os.listdir("/var/log"):
    if log.endswith(".log"):   #startswith(prefix) , endswith(suffix) , replace(old,new) , split , strip , find , lower , upper , os.path.isfile , os.path.isdir , os.path.getsize , os.path.exists
        print(f"Found : {log}")



for i in range(3):
    print(f"Attempt {i+1} to connect")
    time.sleep(2)
