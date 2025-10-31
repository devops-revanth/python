#!/usr/bin/env python3

import os

for log in os.listdir("/var/log"):
    if log.endswith(".log"):
        print(f"Found : {log}")