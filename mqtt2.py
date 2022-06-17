import paho.mqtt.client as mqtt


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("$SYS")   # Subscribing in on_connect() means that if we lose the connection and reconnect then subscriptions will be renewed.

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))



client = mqtt.Client('client1')
client.connect(host="localhost", port=1883, keepalive=60, bind_address="")
client.subscribe("$SYS")
client.publish("$SYS",msg.payload)
client.on_connect = on_connect
clien.on_message = on_message
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
# client.loop_start()
client.loop_forever()
# client.loop_stop()


