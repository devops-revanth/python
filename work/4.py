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

