import psutil
import os

def GetProcessusInfo():
    process = []
    processInfo = []
    
    for p in psutil.process_iter():
        processInfo.append(p.pid)
        processInfo.append(p.name())
        processInfo.append(p.status())
        processInfo.append(p.ppid())
        processInfo.append(p.cmdline())
        process.append(processInfo)
        processInfo = []

    return process

def printInfo():

    print(GetProcessusInfo())