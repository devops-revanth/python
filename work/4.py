#!/usr/bin/env python3

""" def function_name(parameters):
    Docstring: describe purpose
    code block
    return value
"""

# CPU Health Function

def check_cpu(usage):
    if usage > 90:
        return "High CPU Load"
    else:
        return "Load is normal"
    
print(check_cpu(75))
print(check_cpu(92))


# Function Arguments

def greet(name , host):
    print(f"Hello {name}, Welcome to {host}")

greet("admin" , "server01")    #Positional Arguments


#Keywork Arguments

greet(host="server01" , name="root")

#Default Arguments


def restart_service(service="sshd"):
    print(f"Restarting {service} service ...")

restart_service()

restart_service("nginx")


# Return values - A function can return any datatype - string , list , dict or even another function

def get_disk_status(disk_usage):
    if disk_usage > 90:
        return "Critical"
    elif disk_usage > 75:
        return "WARNING"
    else:
        return "OK"
    
status = get_disk_status(88)
print(f"Disk status: {status}")



## Local variable - Global Variable
# Defined inside a function -> only usable within that function

def check_user():
    user = "admin" # local variable
    print(f"{user}")
        

hostname = "server01"
def show_host():
    print(f"{hostname}")  #global variable

show_host()


count = 0
def increment():
    global count
    count += 1

increment()
print(count)
