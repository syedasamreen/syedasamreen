import os
import sys
import subprocess
import pandas as pd
from influxdb import DataFrameClient

def get_cinfig():
    with open('/home/syedasamreen/config.txt') as f:
        lines = f.readlines()
        ip = lines[0]
        user = lines[1]
        pwd = lines[2]
        protocol = lines[-1]
        f.close()
    return ip, user,pwd,protocol
# print(get_cinfig())

def get_ipmi_sensor(ip, user, pwd):
    command = 'ipmitool -I lanplus -H ' + ip + ' -U ' + user + ' -P ' + pwd + ' sdr list'
    ipmi_output = subprocess.getoutput(command)
    return ipmi_output
# print(get_ipmi_sensor)


def get_server_data(ip, user, pwd):
    command1 = 'ipmitool -I lanplus -H ' + ip + ' -U ' + user + ' -P ' + pwd + ' sdr list'
    ipmi_output1 = subprocess.getoutput(command1)
    return ipmi_output1

# def main():
#     ip, protocol = get_cinfig()
#     url = protocol+'://'+ip+'/SmartIoT/src/ajax/getEsxiILODetails.php'
#