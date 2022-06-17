import paho.mqtt.client as mqtt
import time, random
# def on_log(client, userdata,level, buf):
#     print("log: ",buf)
# def on_connect(client, userdata, flags,rc):
#     if rc==0:
#         client.connected_flag = True
#         print("connected ok")
#     else:
#         print("Bad connection returned code =", rc)
#
# mqtt.Client.connected_flag = False
# broker = "test.mosquitto.org"
# # broker = "122.185.109.230"
# client = mqtt.Client("1")
# client.on_connect = on_connect
# client.on_log = on_log
# print("Connecting to the broker",broker)
# # client.loop_start()
# client.connect(broker)
# client.loop_start()
# while not client.connected_flag:
#     print("In wait loop")
#     time.sleep(1)
# print("In main loop")
# client.publish("office/esp32/1")
# time.sleep(4)
# client.loop_stop()
# client.disconnect()

def on_message(client, userdata, message):
    print("message received " ,message.payload.decode("utf-8"))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)

payload = random.randint(0,20)
broker = 'localhost'
client = mqtt.Client('client2')
client.on_message = on_message
client.connect(broker,1883,60)
client.loop_start()
client.subscribe('sensor/epf32')
client.publish('sensor/epf32',payload)

time.sleep(4)
client.loop_stop()
def on_log(client, userdata, level, buf):
    print("log:", buf)
client.on_log = on_log


