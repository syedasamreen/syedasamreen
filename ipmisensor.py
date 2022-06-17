from influx_line_protocol import Metric
f1 =open('/home/syedasamreen/Downloads/ipmidata.txt','r')
line = f1.readline()

l = line.replace('|','')
l1= l.strip().split()
print(l1)
l2 = l1[0]+l1[1]
l3 = l1[2]+''+l1[3]+''+l1[4]
metric = Metric("IPMI_sensor")
metric.with_timestamp(1570977942581909918)
metric.add_tag("Tag",l2)
metric.add_value("value",l3)
metric.add_value("status",l1[5])
print(metric)

