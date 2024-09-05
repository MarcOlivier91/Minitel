import subprocess
import psutil

def getOS():
    release = subprocess.check_output(
    'cat /etc/os-release', shell=True, universal_newlines=True).split("\n")
    return release[0].replace("NAME=", "").replace('"', "")

def getOSversion():
    release = subprocess.check_output(
        'cat /etc/os-release', shell=True, universal_newlines=True).split("\n")
    return release[1]
    
def getUptime():
    tempo = subprocess.check_output(['uptime']).decode('utf-8').replace("\n", "").split(",")
    return tempo[0]

def getKernelVersion():
    return subprocess.check_output('uname -v', shell=True, universal_newlines=True).replace("\n", "")
