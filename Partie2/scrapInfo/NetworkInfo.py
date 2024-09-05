import subprocess

def GetIP():
    ip = subprocess.check_output(
        'hostname -I', shell=True, universal_newlines=True).split("\n")
    return ip

def GetInterfaces():
    interfaces = subprocess.check_output(
        'ip link show', shell=True, universal_newlines=True).split("\n")
    return interfaces

def GetPackets():
    packets = subprocess.check_output(
        'cat /proc/net/dev', shell=True, universal_newlines=True).split("\n")
    return packets

def GetRoutes():
    routes = subprocess.check_output(
        'ip route', shell=True, universal_newlines=True).split("\n")
    return routes

def GetFwdPackets():
    fwdpackets = subprocess.check_output(
        'sysctl net.ipv4.ip_forward', shell=True, universal_newlines=True).split("\n")
    return fwdpackets