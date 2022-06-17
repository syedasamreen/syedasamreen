#
# f = open('/home/syedasamreen/Downloads/ipmidata.txt','r')
# file = f.readlines()
# f.close()
# parsed_data = [line.strip().split('|') for line in file]
# print(parsed_data[0])
from influxdb import InfluxDBClient
from line_protocol_parser import parse_line
# from datetime import datetime
# from influx_line_protocol import Metric,MetricCollection
# f1 =open('/home/syedasamreen/Downloads/ipmidata.txt','r')
# # line = f1.readline()
# # # line = next(line)
# #
# # l = line.replace('|','')
# # l1= l.strip().split()
# # print(l1)
# # l2 = l1[0]+l1[1]
# # l3 = l1[3]+''+l1[4]
# # metric = Metric("IPMI_sensor")
# # metric.with_timestamp(16478669490000)
# # metric.add_tag("Tag",l2)
# # metric.add_value("value",l1[2])
# # metric.add_value("unit",l3)
# # metric.add_value("status",l1[5])
# # print(metric)
# l =  f1.readlines()
# # if l1[1] == 'Temp':
# #     print(l1)
# data = []
# for l1 in l:
#     l1 = l1.strip().split('|')#;print(l1[2])
#     l2 = l1[0].strip().split(' ')#;print(l2[0])
#     l2 = '_'.join(l2)#;print(l2)
#     l3 = l1[1].strip().split()#;print(l3[0])
#     l33 = l3[1:]
#     l4 = '_'.join(l33)#;print(l4)
#     l5 = l1[2]#;print(l5)
#     metric = Metric("IPMI_sensor")
#     metric.with_timestamp(16478669490000)
#     metric.add_tag("Tag",l2)
#     metric.add_value("value",l3[0])
#     metric.add_value("unit",l4)
#     metric.add_value("status",l5)
#     dt = parse_line(metric)
#     data.append(dt)
#
# print(data)
# client = InfluxDBClient('localhost',8086, 'IPMIsensor_data')
# client.create_database('IPMIsensor_data')
# client.write_points(data)














