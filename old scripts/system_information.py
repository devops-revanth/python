import os
import platform
import datetime
import socket


#OS Information
print("OS Type     :" , os.name)
print("System name:" , platform.system())
print("Node Name:" , platform.node())
print("Release:" , platform.release())
print("Version :" , platform.version())
print("Architecture :" , platform.machine())
print("Processor : " , platform.processor())


#Uptime
uptime_seconds = float(os.popen("cat /proc/uptime").read().split()[0])


#Load Average


# IP Address



