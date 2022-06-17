import os
import time
import pandas as pd
import numpy as np
from datetime import datetime, timedelta,timezone
import sys
import requests as req
import subprocess
from datetime import datetime, timedelta, timezone
import time
st = time.time()-time.time()
print(st)
# def get_server_time(times,date):
#     Time = []
#     dt = datetime.striptime(date, '%Y-%m-%d %H-%M-%s')
#     dt = dt.replace(tzinfo = timezone.utc).astimezone(tz = None)
#     for t in times:
#         x = dt + timedelta(seconds=t)
#         Time.append(x)
#     return Time
# server_time = get_server_time(times,date)
# tt = server_time[x].timestamp()*1000000000
# print(tt)
# Host = '10.1.0.29'
# passwd = 'IDRAC@v!gy@nlabs'
# usr = 'root'
# protocol = 'line'
# command_1 = 'ipmitool -I lanplus -H '+Host+' -U '+usr+' -P '+passwd+' sdr list'
#
# out= subprocess.getoutput(command_1)

# import datetime
# print(datetime.datetime.now())
# # print(datetime.datetime.now(timezone.utc))