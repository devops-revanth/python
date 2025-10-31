#!/usr/bin/env python3

"""
if condition:
    #code_block
elif another_condition:
    #code_block
else:
    #default block

"""

#Disk Usage Alert

disk_usage = 85

if disk_usage>90:
    print(f"Critical : Disk Usage above 90#")
elif disk_usage>85:
    print(f"Warning : Disk usage above 80%")
else:
    print(f"OK : Disk usage is normal")

#SSHD server check
service="sshd"
status="running"

if status == "running":
    print(f"{service} is active")
else:
    print(f"{service} is down!")

#Nested conditions
cpu = 70
mem = 85

if cpu > 80:
    if mem>70:
        print(f"High CPU amd Memory utilization")



#Loops
mounts=["/","/home","/data"]

for m in mounts:
    print(f"Disk utilization of {m}")


usage={"cpu":70, "mem":60 , "disk":85}
for key, value in usage.items():
    print(f"{key.upper()} usage = {value}%")

import time
service_up = False
attempt = 0
while not service_up and attempt < 5:
    print(f"Checking service status ...")
    attempt += 1
    time.sleep(2)

print(f"Service check completed")

servers = ["web1","db1","cache1"]
for s in servers:
    if s == "db1":
        print(f"{s} found! Stopping search")
        break

processes = ["sshd","systemd","zombie","nginx"]

for p in processes:
    if p == "zombie":
        continue
    print(f"Monitoring process: {p}")


for i in range(1,6):
    print(f"Checking system{i}")


servers=["web1","db","backup"]
servers.append("frontend")
for index, name in enumerate(servers, start=2):
    print(f"{index}.{name}")