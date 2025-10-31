#!/usr/bin/env python3

#cpu_count = 8  -- int
#load = 2.7    -- float
#str "eth0"   - string
# is_active = true  -- bool
# ["/","/data","/backup"] -- list mount points
# ("eth0" , "UP")  -- tuple - immutable pairs
# { "cpu":45 , "mem":70}  - dict Metrics Key value pair
#  {"server1" , "server2"} - set - Unique hosts set

#type(var) - to verify fata type quickly



service = "sshd"
log = f"/var/log/{service}.log"

print(log)

for service in ["sshd" , "nginx" , "mysql"]:
    log_path=f"/var/log/{service}.log"
    print(log_path)


output = "CPU usage : 45%"
usage = output.split(":")[1].strip().replace("%","")
print(int(usage))

output = "CPU utilization is : 45%"

usage = output.split(":")[1].strip().replace("%","")
print(int(usage))



#lists

mounts = ["/" , "/tmp" , "/data" , "/home"]

for m in mounts:
    print(f"checking the disk usage : {m}")