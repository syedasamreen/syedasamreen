from datetime import datetime, timezone
import os
from influx_line_protocol import Metric

# ## Read ipmidata.txt file
with open('/home/syedasamreen/Downloads/ipmidata.txt','r') as f:
    data =  f.readlines()
    f.close()
## writing output file
file ="ipmi_parsed.txt"
out =open(file, 'a+')

## current time
local_time = datetime.now(timezone.utc).astimezone()
dt = datetime.strftime(local_time, '%Y-%m-%d %H:%M:%S')
## parsing to line protocol
for sensor in data:
    l1 = sensor.strip().split('|')
    l2 = l1[0].strip().split(' ')
    tag = '_'.join(l2)
    l3 = l1[1].strip().split()
    value = l3[0]
    l4 = l3[1:]
    unit = '_'.join(l4);status = l1[2]
    metric = Metric("IPMI_sensor")
    metric.add_tag("Tag", tag)
    metric.add_value("value", value)
    metric.add_value("unit", unit)
    metric.add_value("status", status)
    metric.add_value("timestamp",dt)
    out.write("%s\n" % metric)

out.close()

## file insertion to influxdb
protocol = 'http'
ip ='localhost'
port = '8086'
comm = "curl -i -XPOST '"+protocol+"://"+ip+":"+port+"/write?db=sensor' --data-binary @"+file
os.system(comm)
