import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

mqttBroker ="122.185.109.230"

client = mqtt.Client("Temperature")
client.connect(mqttBroker)

while True:
    randNumber = uniform(20.0, 21.0)
    client.publish("TEMPERATURE", randNumber)
    print("Just published " + str(randNumber) + " to topic TEMPERATURE")
    time.sleep(1)

