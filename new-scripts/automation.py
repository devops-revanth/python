import paramiko

servers = ['10.0.0.1', '10.0.0.2']
for host in servers:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username='admin', password='yourpassword')
    stdin, stdout, stderr = ssh.exec_command('df -h | grep /data')
    print(host, stdout.read().decode())
    ssh.close()


#Remote Command Execution via SSH
import paramiko

servers = ['10.0.0.1', '10.0.0.2']
for host in servers:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username='admin', password='password')
    stdin, stdout, stderr = ssh.exec_command('df -h | grep /data')
    print(f"{host}:\n{stdout.read().decode()}")
    ssh.close()


#Parallel Execution for Fleet
import paramiko
from concurrent.futures import ThreadPoolExecutor

servers = ['10.0.0.1','10.0.0.2','10.0.0.3']

def check_disk(host):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username='admin', password='password')
    stdin, stdout, stderr = ssh.exec_command('df -h | grep /data')
    print(f"{host}:\n{stdout.read().decode()}")
    ssh.close()

with ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(check_disk, servers)



#Monitoring CPU & Memory
import psutil

cpu = psutil.cpu_percent(interval=1, percpu=True)
mem = psutil.virtual_memory()
disk = psutil.disk_usage('/data')

print("CPU Usage:", cpu)
print("Memory Usage:", mem.percent)
print("Disk Usage /data:", disk.percent)




#Logging and Alerts
import logging
import smtplib
from email.message import EmailMessage

logging.basicConfig(filename='/var/log/auto_monitor.log', level=logging.INFO)

disk_usage = 85  # Example value

if disk_usage > 80:
    logging.warning(f"Disk usage high: {disk_usage}%")
    msg = EmailMessage()
    msg.set_content(f"Alert: Disk usage is {disk_usage}%")
    msg['Subject'] = 'Disk Alert'
    msg['From'] = 'monitor@example.com'
    msg['To'] = 'admin@example.com'
    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()



#Parsing Logs & Generating Reports
import pandas as pd

logs = pd.read_csv('/var/log/nginx/access.log', sep=' ', header=None,
                   names=['ip','dash1','dash2','time','request','status','size','ref','ua'])
summary = logs.groupby('status').size()
print(summary)


#Config Automation with YAML
import yaml
import paramiko

with open('servers.yaml') as f:
    servers = yaml.safe_load(f)['servers']

for s in servers:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(s['host'], username=s['user'], password=s['pass'])
    ssh.exec_command('uptime')
    ssh.close()



#Python version with alerts:
import psutil, smtplib
from email.message import EmailMessage

disk_usage = psutil.disk_usage('/var/log').percent
if disk_usage > 85:
    msg = EmailMessage()
    msg.set_content(f"Alert: /var/log usage at {disk_usage}% - Cleanup executed")
    msg['Subject'] = "Disk Alert"
    msg['From'] = "monitor@example.com"
    msg['To'] = "admin@example.com"
    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()




#Python script using psutil:
import psutil, subprocess

services = ["nginx", "mysql"]

for s in services:
    service_running = any(p.info['name'] == s for p in psutil.process_iter(['name']))
    if not service_running:
        subprocess.run(["systemctl", "restart", s])
        print(f"{s} restarted automatically")



#GPU Node Monitoring (Python + paramiko)
import paramiko, smtplib
from email.message import EmailMessage

servers = ["gpu01", "gpu02"]
threshold_temp = 85

for host in servers:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username="admin", password="pass")
    stdin, stdout, stderr = ssh.exec_command("nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader,nounits")
    temp = int(stdout.read().decode().strip())
    if temp > threshold_temp:
        msg = EmailMessage()
        msg.set_content(f"GPU temp {temp}°C on {host} exceeded threshold")
        msg['Subject'] = "GPU Alert"
        msg['From'] = "monitor@example.com"
        msg['To'] = "gpu-admin@example.com"
        s = smtplib.SMTP('localhost')
        s.send_message(msg)
        s.quit()
    ssh.close()
