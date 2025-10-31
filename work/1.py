#!/usr/bin/env python3

import os
hostname = "auto2"
cpu_threshold = 85

"""
This is for learning python3 for Revanth Kumar G
will practice all , one by one
"""

username = input("Enter you name : ")
print(f"You name is : {username}")


hostname = os.uname()[1]

print(f"Your running hostname is : {hostname}")