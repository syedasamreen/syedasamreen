import os
from influx_line_protocol import Metric
import datetime
# #
# f1 =open('/home/syedasamreen/Downloads/ipmidata.txt','r')
# l =  f1.readlines()
# f1.close()
# data = 'IPMI_Sensor3.txt'
# f2 = open(data,'w+')
# # time = str(datetime.datetime.now())
# dt = datetime.datetime.now()
# strp = datetime.datetime.strftime(dt,'%Y-%m-%d %H:%M:%S')
# # print(strp)
# measuremnt = "IPMI_sensor"
# # print(time)
# def sensor_prs():
#     for l1 in l:
#         l1 = l1.strip().split('|')#;print(l1[2])
#         l2 = l1[0].strip().split(' ')#;print(l2[0])
#         l2 = '_'.join(l2)#;print(l2)
#         l3 = l1[1].strip().split()#;print(l3[0])
#         l33 = l3[1:]
#         l4 = '_'.join(l33)#;print(l4)
#         l5 = l1[2]#;print(l5)
#         l6 = measuremnt+','+"Tag="+l2+' '+"Value="+l3[0]+','+"Unit="+l4+','+"Status="+l5+' '+strp
#         return sensor_prs()
#     metric = Metric("IPMI_sensor")
#     metric.with_timestamp(time)
#     metric.add_tag("Tag",l2)
#     metric.add_value("value",l3[0])
#     metric.add_value("unit",l4)
#     metric.add_value("status",l5)
#     f2.write("%s\n" % l6)
# f2.close()
# # protocol = 'http'
# # IP = 'localhost'
# # port = '8086'
# # command = "curl   -i -XPOST '"+protocol+"://"+IP+":"+port+"/write?db=sensor' --data-binary @"+data
# # os.system(command)
# #
# # # command = "curl -k -s -i -XPOST '"+protocol+"://"+ip+"/influx/write?&db=vipl&u="+Influxuser+"&p="+Influxpasswd+"' --data-binary @"+name
# #
#
# print(sensor_prs())

dt = datetime.datetime.utcnow()
crt_tm = datetime.datetime.strftime(dt, '%Y-%m-%d %H:%M:%S')

dtt =


# my_date_format = datetime.strftime(dt, '%Y-%m-%dT%H:%M:%S.%fZ')# is recognized like a string
#
# my_date_format = dt.timestamp() * 100
