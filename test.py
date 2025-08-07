print("Hello Linux admin!")

print("We are creating System Monitoring Script")

log_path="/var/log/messages"
# print(type(log_path))
hostname="mytestvm"
# print(type("mytestvm"))

print("Disk Usage is High")

# name=input("Enter your server name: ")
# print("Running health check on: ", name)

cpu=80

if cpu > 90:
    print("CPU utilization is High")
elif cpu > 70:
    print("Cpu utilization reached warning stage")
else:
    print("CPU utilization is under threshold")


disks=["/" , "/boot"]
for d in disks:
    print("Checking the disks:" , d)



count=0

while count < 3:
    print("Checking logs...")
    
    count += 1 # same as "count = count + 1"


