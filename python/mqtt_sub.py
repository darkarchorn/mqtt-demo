import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

def on_message(client, userdata, message):
    print("Recieved message: ", str(message.payload.decode("utf-8")))

mqttBroker = "mqtt.eclipseprojects.io"
#dat ten cho client
client = mqtt.Client("Smartphone")
#ket noi toi broker
client.connect(mqttBroker)
#client.connect("192.168.11.1",1883)

client.loop_start()
client.subscribe("TEMPERATURE")
client.on_message = on_message
time.sleep(30)
client.loop_stop()
