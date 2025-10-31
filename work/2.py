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


#tuple
iface = ("eth0","UP")
print(f"{iface[0]} status {iface[1]}")


#Dict
server_stats = {"cpu":65, "mem":72,"disk":81}
print(f"Disk Usage: {server_stats['disk']}%")
print(f"Cpu usage : {server_stats['cpu']}%")
print(f"Memory usage : {server_stats['mem']}%")

#set
servers = {"node1" , "node2" , "node3"}
print(f"{servers}")


"""
Arithmetic - +,-,/,%,//,** - Disk Usage Calculations
Comparison -> == != > < >= <= - threshold checks
Logical and or not   - Multi Condition tests
Assignment = += -= *=  - update values
Membership  - in notin   - check item in list/dict
identity -- is , isnot   - compare object refs
Bitwise - & - ^ ~ << >>
"""


disk_usage = 82
if disk_usage > 80:
    print("ALERT: Disk usage is Critical")


cpu=75
mem=70
if cpu>70 and mem>60:
    print(f"High Load Detected")



#List 
servers=["web1" , "web2"]
servers.append("db1")
print(f"{servers}")


"""
strings
lists
numbers
dictionaries
"""