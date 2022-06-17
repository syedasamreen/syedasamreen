import psutil
import libvirt
import datetime
import pandas as pd
conn=libvirt.open("qemu+SSH://root@10.1.0.150/system")
host = conn.getHostname()
print('Hostname:'+host)
fr = psutil.cpu_freq(conn)
for i in fr.keys():
     print(i,fr[i])
print(fr.datetime.now())
# stats = conn.getCPUStats(0)
# print(stats)
# for keys,value in stats:
#     print(stats)
# buf = conn.getMemoryStats(libvirt.VIR_NODE_MEMORY_STATS_ALL_CELLS)
# print(buf)
# dsk = psutil.disk_io_counters(conn)
# # print("DISK i/o")
# # df1 = pd.DataFrame(dsk,columns=['read_count','write_count','read_bytes','write_bytes','read_time','write_time','read_merged_count','write_merged_count','busy_time'])
#
# ntk = psutil.net_io_counters(conn)
# # print("NETWORK i/o")
# # df = pd.DataFrame(ntk,index=['bytes_sent','bytes_recv','packets_sent','packets_recv','errin','errout','dropin','dropout'])
# DF= pd.concat(fr,stats,buf)
# DF.to_csv('NKVM')
# print(DF)
