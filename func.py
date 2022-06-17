# def my_function(fname, lname):
#   print(fname + " " + lname)
#
# my_function("Emil", "Refsnes")
# import sys
# # print(sys.argv)
# import glob
# print(glob.glob('.*py'))
# import echo
# float1 = 546.33
# print("{:5.2f}".format(float1))
# float2 = 546.3345
# print("%5.2f" % float2)
import paho.mqtt.client as mqtt
def on_connect(client,userdata, flags,rc):
    print("connected with source code "+ str(rc))
    client.subscribe("$sys/#")

def on_message(client,userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("mqtt.eclipseprojects.io", 1883,60)
client.loop_forever()