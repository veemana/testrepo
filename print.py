import subprocess
import socket
print(socket.gethostname())

def uptime1():
    raw = subprocess.check_output('uptime').decode("utf8").replace(',', '')
    days = int(raw.split()[2])
    if 'min' in raw:
        hours = 0
        minutes = int(raw[4])
    else:
        hours, minutes = map(int,raw.split()[4].split(':'))
    totalsecs = ((days * 24 + hours) * 60 + minutes) * 60
    return totalsecs

def uptime2():  
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
        return uptime_seconds

uptime1
uptime2
