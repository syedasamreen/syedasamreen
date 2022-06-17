import random
import time
from paho.mqtt import client as mqtt_client

broker = 'localhost'
port = 1883
topic = "$SYS"
# client_id = f'python-mqtt-{random.randint(0, 1000)}'
# username = 'ipmiot'
# password = 'Vigyan12#'
client = mqtt_client.Client("Cl1")
client.connect(broker)
client.subscribe(topic)
client.publish(topic,payload=None)
client.loop_start()
# client.on_connect = on_connect
def on_message(client, userdata, message):
    print("message received " ,message.payload.decode("utf-8"))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
client.on_message = on_message

client.loop_stop()