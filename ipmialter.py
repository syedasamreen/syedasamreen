import os
import requests as req
import pandas as pd
from datetime import datetime, timedelta, timezone
import numpy as np
import time
import sys
import subprocess

req.packages.urllib3.disable_warnings()
DEBUGFLAG = False

# ****** decrypt function
def decrypt_text(ciphertext):
	command = "echo " + ciphertext + " | openssl enc -aes-256-cbc -d -a  -pass pass:b9e8t7e6l5g4e3u2s1e"
	plaintext = subprocess.getoutput(command)
	return plaintext

# ********* get server ip and http or https ****
def get_conf():
	with open('Configure.txt') as fp:
		lines = fp.readlines()
		i = 0
		ipa = lines[0][:-1]
		ip = decrypt_text(ipa)
		protocol = lines[1].rstrip("\n")
		fp.close()
	return ip, protocol

# ************ add seconds to the api time
def get_server_time(times, date):
	Times = []
	dt = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
	dt = dt.replace(tzinfo=timezone.utc).astimezone(tz=None)
	for t in times:
		X = dt + timedelta(seconds=t)
		Times.append(X)
	return Times

def get_server_power(s_ip, s_user, s_pssw):
    avg_power = 0
    command1 = '/usr/bin/ipmitool -I lanplus -H '+s_ip+' -U '+s_user+' -P '+s_pssw+' dcmi power reading'
    if DEBUGFLAG:
        print(command1)
    try:
        reading_txt = subprocess.getoutput(command1)
        if DEBUGFLAG:
            print(reading_txt)
            print('************************')
        for line in reading_txt.split('\n'):
            if 'DCMI request failed because: Command not supported in present state' in line:
                if DEBUGFLAG:
                    print(s_ip,' : POWER METER MISSING')
                break
            elif 'Instantaneous power reading:' in line:
                xx1 = line.split(' ')
                avg_power = float(xx1[-2])
    except:
        if DEBUGFLAG:
            print(s_ip,' : POWER READING Problem')
    return avg_power


# ***** main function
def main():
	global DEBUGFLAG
	if len(sys.argv) > 1:
		if sys.argv[1] == 'DEBUG':
			DEBUGFLAG = True

	start = datetime.now()
	ip, protocol = get_conf()
	url = protocol + '://' + ip + '/SmartIoT/src/ajax/getEsxiILODetails.php'
	d = {'operation': 'getEsxiILODetails'}
	resp = req.post(url, d, verify=False)
	data = resp.json()


# ***** chassiss variables ********
sys_power, power_overload, power_interlock, main_power_fault, power_cntrl_fault = [], [], [], [], []
power_restore_policy, last_power_event, chassis_intrusion, front_panel_lockout, drive_fault = [], [], [], [], []
cooling_fault, front_panel_cntrl, sleep_btn_disable, sleep_btn_disabled, diag_btn_disable, diag_btn_disabled = [], [], [], [], [], []
reset_btn_disable, reset_btn_disabled, power_btn_disable, power_btn_disabled, serverpower = [], [], [], [], []
# device info variables
devicename, deviceid = [], []
# ****** sensors variables ********
inlet_temp, fan_no, fan, cpu_exhaust, times, cpu_temp = [], [], [], [], [], []
data=[]
i = 0
for server in data:
    if 'ilo_ipaddress' in server:
        hostip_enc = server['ilo_ipaddress']
        if hostip_enc is not None:
            host = decrypt_text(hostip_enc)
            passw = decrypt_text(server['ilo_password'])
            user = server['ilo_username']
        command3 = '/usr/bin/ipmitool -I lanplus -H ' + host + ' -U ' + user + ' -P ' + passw + ' chassis status'
        command4 = '/usr/bin/ipmitool -I lanplus -H ' + host + ' -U ' + user + ' -P ' + passw + ' -v sensor list'
    try:
           chasie_output = subprocess.getoutput(command3)
           sensor_output = subprocess.getoutput(command4)
        if ('Error: Unable to establish IPMI v2 / RMCP+ session' not in sensor_output) or ('Error: Unable to establish IPMI v2 / RMCP+ session' not in chasie_output):
                avgpower = get_server_power(host, user, passw)
                serverpower.append(avgpower)
                devicename.append(server['devicename'])
                deviceid.append(server['deviceid'])

# **** initialize chassis variables to ''
sys_power.append(''), power_overload.append(''), power_interlock.append(''), main_power_fault.append(''), power_cntrl_fault.append('')
power_restore_policy.append(''), last_power_event.append(''), chassis_intrusion.append(''), front_panel_lockout.append('')
drive_fault.append(''), cooling_fault.append(''), front_panel_cntrl.append(''), sleep_btn_disable.append(''), sleep_btn_disabled.append('')
diag_btn_disable.append(''), diag_btn_disabled.append(''), reset_btn_disable.append(''), reset_btn_disabled.append(''), power_btn_disable.append(''), power_btn_disabled.append('')

for line in chasie_output.split('\n'):
	tag = line.split(':')
	val_part = tag[1].split(' ')
	val = val_part[1]
        if 'System Power' in line:
		sys_power[i] = val
        elif 'Power Overload' in line:
	        power_overload[i] = val
        elif 'Power Interlock' in line:
            power_interlock[i] = val
        elif 'Main Power Fault' in line:
            main_power_fault[i] = val
        elif 'Power Control Fault' in line:
            power_cntrl_fault[i] = val
        elif 'Power Restore Policy' in line:
            power_restore_policy[i] = val
        elif 'Last Power Event' in line:
            last_power_event[i] = val
        elif 'Chassis Intrusion' in line:
            chassis_intrusion[i] = val
        elif 'Front-Panel Lockout' in line:
            front_panel_lockout[i] = val
        elif 'Drive Fault' in line:
            drive_fault[i] = val
        elif 'Cooling/Fan Fault' in line:
             cooling_fault[i] = val
        elif 'Front Panel Control' in line:
             front_panel_cntrl[i] = val
        elif 'Sleep Button Disable' in line:
             sleep_btn_disable[i] = val
        elif 'Diag Button Disable' in line:
             diag_btn_disable[i] = val
        elif 'Reset Button Disable' in line:
            reset_btn_disable[i] = val
        elif 'Power Button Disable' in line:
            power_btn_disable[i] = val
        elif 'Sleep Button Disabled' in line:
             sleep_btn_disabled[i] = val
        elif 'Diag Button Disabled' in line:
             diag_btn_disabled[i] = val
        elif 'Reset Button Disabled' in line:
             reset_btn_disabled[i] = val
        elif 'Power Button Disabled' in line:
             power_btn_disabled[i] = val

# ts = datetime.utcnow()
end = datetime.now()
ts = end - start
ts = ts.seconds
times.append(ts)
fan_counter = 0
prev_fanno = ''
prev_sensor_type = ''
fan_out_buffer = ''
# **** initialize sensors variable to ''
inlet_temp.append(0), fan.append(''), cpu_exhaust.append(0), fan_no.append(0), cpu_temp.append(0)

for line in sensor_output.split('\n'):
	if 'Sensor ID: Fan' in line:
		Fan_ID_val = line.split(':')
		fan_tag = Fan_ID_val[1].split(' ')
		if fan_tag[1] == 'Fan':
			if fan_tag[2] != prev_fanno:
			    fan_counter = fan_counter + 1
			    prev_fanno = fan_tag[2]
			    prev_sensor_type = 'Fan'
			else:
				prev_sensor_type = ''
	        else:
		        prev_fanno = fan_tag[1]
		        fan_counter = fan_counter + 1
		        prev_sensor_type = 'Fan'
	        elif 'Inlet' in line:\
		         prev_sensor_type = 'Inlet'
	        elif 'Exhaust' in line:\
                  prev_sensor_type = 'Exhaust'
            elif ('Sensor ID: Temp' in line) or ('Sensor ID: 02-CPU 1' in line):\
	              prev_sensor_type = 'cpu_temp'
            if (prev_sensor_type == 'Fan') and ('Sensor Reading:' in line):
	              reading_tag = line.split(':')
	            if '+/' in reading_tag[1]:
		             readings = reading_tag[1].split(' ')
		             val = readings[1]
		             unit = readings[4]
		             fan_out_buffer = fan_out_buffer + ' ' + prev_fanno + ' ' + val + ' ' + unit
	            else:
		            readings = reading_tag[1].split(' ')
		            val = readings[1]
		            unit = readings[2]
		            fan_out_buffer = fan_out_buffer + ' ' + prev_fanno + ' ' + val + ' ' + unit
	                prev_sensor_type = ''
            elif (prev_sensor_type == 'Inlet') and ('Sensor Reading:' in line):\
	               Inlet_tag = line.split(":")
            if Inlet_tag[1] != "  Unable to read sensor: Device Not Present":
	               if '+/' in Inlet_tag[1]:
		                inlet_readings = Inlet_tag[1].split(' ')
		                val = float(inlet_readings[1])
		                degree = inlet_readings[4]
		                unit = inlet_readings[5]
		                inlet_temp[i] = val
	else:
		inlet_readings = Inlet_tag[1].split(' ')
		val = float(inlet_readings[1])
		degree = inlet_readings[2]
		unit = inlet_readings[3]
		inlet_temp[i] = val
else:
	inlet_temp[i] = 0
	prev_sensor_type = ''
elif (prev_sensor_type == 'Exhaust') and ('Sensor Reading        :' in line):
	Exhaust_tag = line.split(":")
	if '+/' in Exhaust_tag[1]:
		Exhaust_readings = Exhaust_tag[1].split(' ')
		val = float(Exhaust_readings[1])
		degree = Exhaust_readings[4]
		unit = Exhaust_readings[5]
		cpu_exhaust[i] = val
	else:
		Exhaust_readings = Exhaust_tag[1].split(' ')
		val = float(Exhaust_readings[1])
		degree = Exhaust_readings[2]
		unit = Exhaust_readings[3]
		cpu_exhaust[i] = val
	prev_sensor_type = ''
elif (prev_sensor_type == 'cpu_temp') and ('Sensor Reading        :' in line):
	cputemp_tag = line.split(":")
	if '+/' in cputemp_tag[1]:
		cputemp_readings = cputemp_tag[1].split(' ')
		val = float(cputemp_readings[1])
		degree = cputemp_readings[4]
		unit = cputemp_readings[5]
		cpu_temp[i] = val
	else:
		cputemp_readings = cputemp_tag[1].split(' ')
		val = float(cputemp_readings[1])
		degree = cputemp_readings[2]
		unit = cputemp_readings[3]
		cpu_temp[i] = val
	prev_sensor_type = ''

fan_no[i] = int(fan_counter)
fan[i] = fan_out_buffer
i = i + 1


except OSError:
print('ipmitool does not exist')

elif 'passwd' in server:
date = server['date']
Influxuser = decrypt_text(server['uname'])
Influxpasswd = decrypt_text(server['passwd'])
server_time = get_server_time(times, date)

name = 'tempdata.txt'
fp = open(name, 'a+')
for x in range(len(deviceid)):
	tt = server_time[x].timestamp() * 1000000000
	fp.write('IPMI_DATA,deviceid=%d,devicename=%s System_Power="%s",Power=%f,Power_overload="%s",Power_interlock="%s",\
Main_Power_Fault="%s",Power_control_Fault="%s",Power_restore_policy="%s",Chassis_intrusion="%s",Front_panel_lockout="%s",\
Cooling_Fault="%s",Front_panel_control="%s",inlet_temp=%f,Cpu_exhaust=%f,cpu_temp=%f,Drive_Fault="%s",Fan="%s",\
Fan_NO=%d %d\n' % (deviceid[x], devicename[x], sys_power[x], serverpower[x], power_overload[x], power_interlock[x],
				   main_power_fault[x], \
				   power_cntrl_fault[x], power_restore_policy[x], chassis_intrusion[x], front_panel_lockout[x],
				   cooling_fault[x], front_panel_cntrl[x], \
				   inlet_temp[x], cpu_exhaust[x], cpu_temp[x], drive_fault[x], fan[x], fan_no[x], tt))
fp.close()
command = "curl -k -s -i -XPOST '" + protocol + "://" + ip + "/influx/write?&db=vipl&u=" + Influxuser + "&p=" + Influxpasswd + "' --data-binary @" + name
os.system(command)
os.remove(name)

if __name__ == "__main__":
	main()


