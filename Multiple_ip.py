import subprocess
import datetime
from influxdb import InfluxDBClient

# reading ip credentials
with open('/home/syedasamreen/ipcred.txt') as f:
    lines = f.readlines()
    f.close()
out = []
for i in range(0, len(lines)):
    ip = "10.1.0.{0}".format(i)
    usr = lines[5][:-1]
    pwd = lines[6][:-1]
    # print(ip,usr,pwd)
    comm = 'ipmitool -I lanplus -H ' + ip + ' -U ' + usr + ' -P ' + pwd + ' sdr list'
    ch_out = subprocess.getoutput(comm)
    out.append(ch_out)


def get_conf():
    with open('/home/syedasamreen/inflx_cred.config') as fp:
        lns = fp.readlines()
        fp.close()
        usr = lns[0][:-1]
        pwd = lns[1].rstrip('\n')
        db = lns[2].rstrip("\n")
        ipa = lns[3].rstrip("\n")
        port = lns[4].rstrip()
    return usr, pwd, db, ipa, port





def lin_proto():
    for l1 in out:
        l1 = l1.strip().split('|')  # ;print(l1[2])
        tag = l1[0].strip().split(' ')  # ;print(l2[0])
        l2 = '_'.join(tag)  # ;print(l2)
        l3 = l1[1].strip().split()  # ;print(l3[0])
        value = l3[0]
        l33 = l3[1:]
        unit = '_'.join(l33)  # ;print(l4)
        status = l1[2]
        return tag, value, unit, status


tag, value, unit, status = lin_proto()


def get_time():
    dt = datetime.datetime.utcnow()
    crt_tm = datetime.datetime.strftime(dt, '%Y-%m-%d %H:%M:%S')
    return crt_tm


crt_tm = get_time()

data = [
    {
        "measurment": "IPMI_sensor",
        "tags": {
            "host": ipa,
            "Tag": tag
        },
        "time": crt_tm,
        "fields": {
            "value": value,
            "unit": unit,
            "status": status
        }

    }

]


def conn_influx():
    ipa, port, user, pwd, db = get_conf()
    client = InfluxDBClient(ipa, port, user, pwd, db)
    client.create_database(db)
    client.write_points(data, db, protocol='line')
    return
